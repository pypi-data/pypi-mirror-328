"""Flask関連のユーティリティ。"""

import base64
import contextlib
import json
import logging
import pathlib
import secrets
import threading
import typing
import urllib.parse
import xml.etree.ElementTree

import flask
import httpx
import werkzeug.middleware.proxy_fix
import werkzeug.serving
import werkzeug.test

logger = logging.getLogger(__name__)


def generate_secret_key(cache_path: str | pathlib.Path) -> bytes:
    """シークレットキーの作成/取得。

    既にcache_pathに保存済みならそれを返し、でなくば作成する。

    """
    cache_path = pathlib.Path(cache_path)
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    with cache_path.open("a+b") as secret:
        secret.seek(0)
        secret_key = secret.read()
        if not secret_key:
            secret_key = secrets.token_bytes()
            secret.write(secret_key)
            secret.flush()
        return secret_key


def data_url(data: bytes, mime_type: str) -> str:
    """小さい画像などのバイナリデータをURLに埋め込んだものを作って返す。

    Args:
        data: 埋め込むデータ
        mime_type: 例：'image/png'

    """
    b64 = base64.b64encode(data).decode("ascii")
    return f"data:{mime_type};base64,{b64}"


def get_next_url() -> str:
    """flask_loginのnextパラメータ用のURLを返す。"""
    path = flask.request.script_root + flask.request.path
    query_string = flask.request.query_string.decode("utf-8")
    next_ = f"{path}?{query_string}" if query_string else path
    return next_


def get_safe_url(target: str | None, host_url: str, default_url: str) -> str:
    """ログイン時のリダイレクトとして安全なURLを返す。"""
    if target is None or target == "":
        return default_url
    ref_url = urllib.parse.urlparse(host_url)
    test_url = urllib.parse.urlparse(urllib.parse.urljoin(host_url, target))
    if test_url.scheme not in ("http", "https") or ref_url.netloc != test_url.netloc:
        logger.warning(f"Invalid next url: {target}")
        return default_url
    return target


@contextlib.contextmanager
def run(app: flask.Flask, host: str = "localhost", port: int = 5000):
    """Flaskアプリを実行するコンテキストマネージャ。テストコードなど用。"""

    if not any(
        m.endpoint == "_pytilpack_flask_dummy" for m in app.url_map.iter_rules()
    ):

        @app.route("/_pytilpack_flask_dummy")
        def _pytilpack_flask_dummy():
            return "OK"

    server = werkzeug.serving.make_server(host, port, app, threaded=True)
    ctx = app.app_context()
    ctx.push()
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        # サーバーが起動するまで待機
        while True:
            try:
                httpx.get(
                    f"http://{host}:{port}/_pytilpack_flask_dummy"
                ).raise_for_status()
                break
            except Exception:
                pass
        # 制御を戻す
        yield
    finally:
        server.shutdown()
        thread.join()


def assert_bytes(response, status_code: int = 200) -> bytes:
    """flaskのテストコード用。

    Args:
        response: レスポンス
        status_code: 期待するステータスコード

    Raises:
        AssertionError: ステータスコードが異なる場合

    Returns:
        レスポンスボディ

    """
    response_body = response.get_data()

    # ステータスコードチェック
    if response.status_code != status_code:
        logger.info(
            f"ステータスコードエラー: {response.status_code} != {status_code}\n\n{response_body!r}"
        )
        raise AssertionError(
            f"ステータスコードエラー: {response.status_code} != {status_code})"
        )

    return response_body


def assert_html(
    response, status_code: int = 200, tmp_path: pathlib.Path | None = None
) -> str:
    """flaskのテストコード用。

    html5libが必要なので注意。

    Args:
        response: レスポンス
        status_code: 期待するステータスコード

    Raises:
        AssertionError: ステータスコードが異なる場合

    Returns:
        レスポンスボディ (bs4.BeautifulSoup)

    """
    import html5lib

    response_body = response.get_data().decode("utf-8")

    # ステータスコードチェック
    if response.status_code != status_code:
        tmp_file_path = _create_temp_file(tmp_path, response_body)
        raise AssertionError(
            f"ステータスコードエラー: {response.status_code} != {status_code} (HTML: {tmp_file_path} )"
        )

    # HTMLのチェック
    parser = html5lib.HTMLParser(strict=True, debug=True)
    try:
        _ = parser.parse(response.data)
    except html5lib.html5parser.ParseError as e:
        tmp_file_path = _create_temp_file(tmp_path, response_body)
        raise AssertionError(f"HTMLエラー: {e} (HTML: {tmp_file_path} )") from e

    return response_body


def _create_temp_file(
    tmp_path: pathlib.Path | None, response_body: str
) -> pathlib.Path:
    """一時ファイルを作成してパスを返す。"""
    import pytilpack.pytest_

    tmp_file_path = pytilpack.pytest_.tmp_file_path(tmp_path, suffix=".html")
    tmp_file_path.write_text(response_body, encoding="utf-8")
    logger.info(f"HTML: {tmp_file_path}")
    return tmp_file_path


def assert_json(response, status_code: int = 200) -> dict[str, typing.Any]:
    """flaskのテストコード用。

    Args:
        response: レスポンス
        status_code: 期待するステータスコード

    Raises:
        AssertionError: ステータスコードが異なる場合

    Returns:
        レスポンスのjson

    """
    response_body = response.get_data().decode("utf-8")

    # ステータスコードチェック
    if response.status_code != status_code:
        logger.info(
            f"ステータスコードエラー: {response.status_code} != {status_code}\n\n{response_body}"
        )
        raise AssertionError(
            f"ステータスコードエラー: {response.status_code} != {status_code})"
        )

    # Content-Typeチェック
    if response.content_type != "application/json":
        logger.info(
            f"Content-Typeエラー: {response.content_type} != application/json\n\n{response_body}"
        )
        raise AssertionError(
            f"Content-Typeエラー: {response.content_type} != application/json"
        )

    # JSONのチェック
    try:
        data = json.loads(response_body)
    except Exception as e:
        logger.info(f"JSONエラー: {e}\n\n{response_body}")
        raise AssertionError(f"JSONエラー: {e}") from e

    return data


def assert_xml(response, status_code: int = 200) -> str:
    """flaskのテストコード用。

    Args:
        response: レスポンス
        status_code: 期待するステータスコード

    Raises:
        AssertionError: ステータスコードが異なる場合

    Returns:
        レスポンスのxml

    """
    response_body = response.get_data().decode("utf-8")

    # ステータスコードチェック
    if response.status_code != status_code:
        logger.info(
            f"ステータスコードエラー: {response.status_code} != {status_code}\n\n{response_body}"
        )
        raise AssertionError(
            f"ステータスコードエラー: {response.status_code} != {status_code})"
        )

    # Content-Typeチェック
    if response.content_type not in ("application/xml", "text/xml"):
        logger.info(f"Content-Typeエラー: {response.content_type}\n\n{response_body}")
        raise AssertionError(f"Content-Typeエラー: {response.content_type}")

    # XMLのチェック
    try:
        _ = xml.etree.ElementTree.fromstring(response_body)
    except Exception as e:
        logger.info(f"XMLエラー: {e}\n\n{response_body}")
        raise AssertionError(f"XMLエラー: {e}") from e

    return response_body


class ProxyFix(werkzeug.middleware.proxy_fix.ProxyFix):
    """リバースプロキシ対応。

    nginx.conf設定例::
        proxy_set_header X-Forwarded-For $remote_addr;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Forwarded-Port $server_port;
        proxy_set_header X-Forwarded-Prefix $http_x_forwarded_prefix;

    """

    def __init__(
        self,
        flaskapp: flask.Flask,
        x_for: int = 1,
        x_proto: int = 1,
        x_host: int = 0,
        x_port: int = 0,
        x_prefix: int = 1,
    ):
        super().__init__(
            flaskapp.wsgi_app,
            x_for=x_for,
            x_proto=x_proto,
            x_host=x_host,
            x_port=x_port,
            x_prefix=x_prefix,
        )
        self.flaskapp = flaskapp

    def __call__(self, environ, start_response):
        if self.x_prefix != 0:
            prefix = environ.get("HTTP_X_FORWARDED_PREFIX", "/")
            if prefix != "/":
                self.flaskapp.config["APPLICATION_ROOT"] = prefix
                self.flaskapp.config["SESSION_COOKIE_PATH"] = prefix
                self.flaskapp.config["REMEMBER_COOKIE_PATH"] = prefix
                environ["SCRIPT_NAME"] = prefix
                environ["PATH_INFO"] = environ["PATH_INFO"][len(prefix) :]
        return super().__call__(environ, start_response)

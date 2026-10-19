import pytest
import threading
import time
import requests
from app import ThreadingHTTPServer, Handler

@pytest.fixture(scope="module")
def server():
    # 测试期间用 8088 端口，防止和正式服务冲突
    srv = ThreadingHTTPServer(('127.0.0.1', 8088), Handler)
    t = threading.Thread(target=srv.serve_forever)
    t.daemon = True
    t.start()
    time.sleep(1) # 等服务器启动
    yield
    srv.shutdown()

def test_home_page(server):
    response = requests.get("http://127.0.0.1:8088")
    assert response.status_code == 200
    assert "Hello" in response.text

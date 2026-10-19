from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 如果是请求网页图标，直接返回 204 (无内容)，不阻塞主页面
        if self.path == '/favicon.ico':
            self.send_response(204)
            self.end_headers()
            return

        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write("Hello, 这是我的第一个自动化部署的网页！".encode('utf-8'))

if __name__ == '__main__':
    # 换用多线程服务器，解决卡顿问题
    server = ThreadingHTTPServer(('0.0.0.0', 8000), Handler)
    print('多线程服务器运行在 8000 端口...')
    server.serve_forever()

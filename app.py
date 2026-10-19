import datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/favicon.ico':
            self.send_response(204)
            self.end_headers()
            return

        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        
        # 获取当前时间
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        html_content = f"<h1>Hello, 这是一个自动化部署的网页！</h1><p>本次容器启动时间: {now}</p>"
        
        self.wfile.write(html_content.encode('utf-8'))

if __name__ == '__main__':
    server = ThreadingHTTPServer(('0.0.0.0', 8000), Handler)
    print('服务器运行在 8000 端口...')
    server.serve_forever()

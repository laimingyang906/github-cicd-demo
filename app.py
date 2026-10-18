from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        # 等会儿我们会通过自动化部署看到这句话
        self.wfile.write("Hello, 这是我的第一个自动化部署的网页！".encode('utf-8'))

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 8000), Handler)
    print('服务器运行在 8000 端口...')
    server.serve_forever()

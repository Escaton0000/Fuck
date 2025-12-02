# Vercel Serverless Function (Python)
from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        # 요청 본문 읽기
        length = int(self.headers.get('content-length'))
        body = self.rfile.read(length)
        data = json.loads(body)

        text = data.get("text", "")

        # 여기서 원하는 Python 로직 실행
        # 예: 텍스트 뒤집기
        result = text[::-1]

        # 응답 반환
        response = {"result": result}

        # 헤더
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        # JSON 응답
        self.wfile.write(json.dumps(response).encode())

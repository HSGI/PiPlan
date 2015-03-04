import http.server

PORT = 8000

httpd = http.server.HTTPServer(("", PORT), http.server.SimpleHTTPRequestHandler)

print("serving at port", PORT)
httpd.serve_forever()
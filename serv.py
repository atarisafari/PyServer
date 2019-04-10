from http.server import HTTPServer, BaseHTTPRequestHandler

class Serv(BaseHTTPRequestHandler):

	def do_GET(self):
		if self.path == '/':
			self.path = '/index.html'
		try:
			file_to_open = open(self.path[1:]).read()
			self.send_response(200)
		except:
			file_to_open = "File not found"
			self.send_response(404)

		#Required by HTTPRequestHandler class
		self.end_headers()

		#Write file contents to screen by converting text file to bytes
		self.wfile.write(bytes(file_to_open, 'utf-8'))

#Create httpd variable using HTTPServer class and pass in our Serv class
httpd = HTTPServer(('localhost', 8080), Serv)

#
httpd.serve_forever()

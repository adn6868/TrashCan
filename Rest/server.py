import socket

ENCODING = "utf-8"
PORT = 5

class Server:
	"""docstring for Server"""
	def __init__(self):
		self.ip = socket.gethostbyname(socket.gethostname())
		self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.port = PORT
	def addMessage(self,message):
		self.m = bytes(message,ENCODING)
	def sendMessage(self,destination,port):
		self.s.sendto(self.m,(destination,port))
	def listen(self):
		self.s.bind(("",self.port))
		self.s.listen()
		while True:
			c, addr = self.s.accept()
			print('got connection from', addr)
			print('he send: ', self.s.recv(1024).decode(ENCODING))
			c.sendMessage(self,addr,self.port)

	def getIp(self):
		return self.ip

def main():
	s = Server()
	print("Init Server")
	print("Server Inet address:", s.getIp())
	s.addMessage("This is the server!")
	print("Start listening:")
	s.listen()

if __name__ == '__main__':
	main()
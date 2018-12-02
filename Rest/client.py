import socket


ENCODING = "utf-8"
PORT = 5

class Client:
	def __init__(self):
		self.ip = socket.gethostbyname(socket.gethostname())
		self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.port = PORT
	def addMessage(self,message):
		self.m = bytes(message,ENCODING)
	def sendMessage(self,destination,port):
		self.s.sendto(self.m,(destination,port))

	def getIp(self):
		return self.ip


def main():
	Client = Client()

if __name__ == '__main__':
	main()

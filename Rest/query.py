import socket
class Query:
	"""docstring for Query"""
	def __init__(self, query):
		self.q = query
	def toString(self):
		return "Query request by: "+ string(self.q)
		
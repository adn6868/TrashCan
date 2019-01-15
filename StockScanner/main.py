import requests
import time
import threading
import concurrent.futures
import json

class MyULF:
	"""docstring for MyULF"""
	def __init__(self, key = 'EBBVJ2TH7C8Y5HEA'):
		self.key = key
		self.header = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=5min&outputsize=full&apikey='
		self.symbol = ''
		self.interval = ''
		self.outputsize = ''
		self.VALID_INTERVAL = ['1min','5min']

	
	def setSymbol(self, symbol):
		self.symbol = symbol.upper()
	def setInterval(self,interval = "1min"):
		if interval in self.VALID_INTERVAL:
			self.interval = interval
		elif not self.interval:
			self.interval = self.VALID_INTERVAL[0]
	def setOutputSize(self,size = "full"):
		self.outputsize = size
	def getURL(self):
		if self.symbol:
			return  "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={0}&interval={1}&outputsize={2}&apikey={3}".format(self.symbol,self.interval,self.outputsize,self.key)
		pass
		
# string s = string.Format("Hey, {0} it is the {1}st day of {2}.  I feel {3}!", _name, _day, _month, _feeling);

if __name__ == '__main__':
	url = MyULF()
	url.setInterval()
	url.setOutputSize()
	symbolList = [ "GOOGL" , "AAPL" , "CRON" , "DNR"]
	for s in symbolList:
		url.setSymbol(s)
		data = requests.get(url = url.getURL()).json()
		with open(s+'.txt','w') as f:
			json.dump(data, f)

	# print(json.dump(get("AAPL"),indent= 2))
import requests
import time
import threading
import concurrent.futures
import json

class UrlBuilder:
	def __init__(self, key = 'EBBVJ2TH7C8Y5HEA'):
		self.key = key
		self.symbol = ''
		self.function = ''
		self.interval = ''
		self.outputsize = ''
		self.VALID_FUNCTIONS = ''
		self.VALID_INTERVALS = ['1min','5min']

	def setSymbol(self, symbol):
		self.symbol = symbol.upper()
	def setInterval(self,interval = "5min"):
		if interval in self.VALID_INTERVALS:
			self.interval = interval
		elif not self.interval:
			self.interval = self.VALID_INTERVALS[0]
	def setOutputSize(self,size = "full"):
		self.outputsize = size
	def getURL(self):
		if self.symbol:
			return  "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={0}&interval={1}&outputsize={2}&apikey={3}"\
			.format(self.symbol,self.interval,self.outputsize,self.key)
		pass

if __name__ == '__main__':
	urlBuilder = UrlBuilder()
	urlBuilder.setInterval()
	urlBuilder.setOutputSize()
	symbolList = [ "TLRY" , "AAPL" , "CRON" , "DNR"]
	for s in symbolList:
		urlBuilder.setSymbol(s)
		data = requests.get(url = urlBuilder.getURL()).json()
		with open('data/'+s+'.json','w') as f:
			json.dump(data, f,indent=2)
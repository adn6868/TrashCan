from sys import stdout as O
import concurrent.futures
import json
import requests
import threading
import time

NUMBER_OF_THREAD = 5
KEY = 'EBBVJ2TH7C8Y5HEA'
INPUT_FILE = 'symbolList.txt'

class UrlBuilder:
	'''
	Update this to match API
	'''
	def __init__(self, key = KEY):
		self.function = ''
		self.interval = ''
		self.key = key
		self.outputsize = ''
		self.symbol = ''
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

LOCAL_THREAD = threading.local()

def thread_requests():
	if not getattr(LOCAL_THREAD,"requests",None):
		LOCAL_THREAD.requests = requests
	return LOCAL_THREAD.requests

def thread_UrlBuilder():
	if not getattr(LOCAL_THREAD,"urlBuilder",None):
		LOCAL_THREAD.urlBuilder = UrlBuilder()
	return LOCAL_THREAD.urlBuilder

def download(symbol):
	O.write("Downloading: {0} \n".format(symbol))
	urlBuilder = thread_UrlBuilder()
	urlBuilder.setSymbol(symbol)
	requests = thread_requests()
	data = requests.get(url = urlBuilder.getURL()).json()
	O.write("Download success: {0} \n".format(symbol))
	with open('data/'+symbol+'.json','w') as f:
		json.dump(data, f,indent=2)

def download_list(symbolList):
	with concurrent.futures.ThreadPoolExecutor(max_workers = NUMBER_OF_THREAD) as executor:
		executor.map(download, symbolList)

if __name__ == '__main__':
	with open(INPUT_FILE,'r') as f:
		symbolList = f.read().split('\n')
	
	startTime = time.time()
	download_list(symbolList)
	duration = time.time() - startTime
	print("download %d symbols in %s seconds " % (len(symbolList),str(duration)) )

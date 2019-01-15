import requests
import time


def get(url, session):
	with session.get(url) as response:
		print("get %d from %s" % (len(response.content), url))
		# pass

def getList(sites):
	with requests.Session() as session:
		for url in sites:
			get(url,session)

if __name__ == '__main__':
	print("Naive Single processing:")
	sites = ['http://google.com', 'http://apple.com'] * 10
	startTime = time.time()
	getList(sites)
	duration =time.time()-startTime
	print("download %d in %s seconds " % (len(sites),str(duration)) )

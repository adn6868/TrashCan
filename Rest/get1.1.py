import requests
import time
import threading
import concurrent.futures

LOCAL_THREAD = threading.local()

def thread_session ():
	if not getattr(LOCAL_THREAD, "session", None):
		LOCAL_THREAD.session = requests.Session()
	return LOCAL_THREAD.session

def get(url):
	session = thread_session()
	with session.get(url) as response:
		print("get {0} from {1}".format(len(response.content), url))

# def getList(sites):
# 	with requests.Session() as session:
# 		for url in sites:
# 			get(url,session)

def getList(sites):
	with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
		executor.map(get, sites)


if __name__ == '__main__':
	print("Threading:")
	sites = ['http://google.com', 'http://apple.com'] * 10
	startTime = time.time()
	getList(sites)
	duration =time.time()-startTime
	print("download %d in %s seconds " % (len(sites),str(duration)) )
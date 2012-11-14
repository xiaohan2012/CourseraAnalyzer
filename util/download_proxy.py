from urllib2 import Request,urlopen
from threading import Thread
from Queue import queue 

class DownloadProxy():
    worker_number = 5
    def __init__(self):
        pass

    @staticmethod
    def download(url,headers = {},data = {}):
        pass

class DownloadWorker(Thread):
    def __init__(self):
        Thread.__init__(self)
    
    def run(self):



from config import *
from os import path

class RequestHeaders(dict):
    def __init__(self,course_short_name,data={}):
        dict.__init__(self, data)
        self._load_req_headers(course_short_name)

    def _load_req_headers(self,course_short_name):
        with open(path.join(req_data_path,course_short_name),"r") as f:
            self["url"] = f.readline().strip()
            for l in f.readlines():
                key,val = l.strip().split(":",1)
                self[key] = val
            del self["Accept-Encoding"] 

    def get_url(self):
        url = self["url"]
        del self["url"]
        return url

if __name__ == "__main__":
    req_d = RequestHeaders("pgm")
    print req_d
        
        

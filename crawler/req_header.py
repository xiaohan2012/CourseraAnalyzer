from coursera.config import *
from os import path

class RequestHeader(dict):
    def __init__(self,course_short_name,header_type,data={}):
        dict.__init__(self, data)
        self._load_req_headers(course_short_name,header_type)

    def _load_req_headers(self,course_short_name,header_type):
        with open(path.join(req_data_path,header_type,course_short_name+".txt"),"r") as f:
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
    req_d = RequestHeader("design-2012-001","forum")
    print req_d
        
        

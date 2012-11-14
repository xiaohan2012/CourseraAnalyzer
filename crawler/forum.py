import os

from pyquery import PyQuery as pq
from urllib2 import Request, urlopen
from hashlib import sha1
from StringIO import StringIO

from util.req_header import RequestHeaders
from config import *

class CourseForumPage(pq):
    def __init__(self,*args,**kwargs):
        pq.__init__(self,*args, **kwargs)#shrug my shoulder..

    @staticmethod
    def instantiate():
        return CourseForumPage(StringIO())

    def load_page(self,course_short_name,save_to_local = True):
        rd = RequestHeaders(course_short_name)
        self.url = rd.get_url()
        if self._local_cache_exist():#if already cached 
            doc = open(self._get_cache_path(),"r").read()
        else:
            req = Request(self.url,headers = dict(rd))
            res = urlopen(req)
            doc = res.read()
            if save_to_local: #cache it
                f = open(self._get_cache_path(),"w")
                f.write(doc)
                f.close()
        CourseForumPage.__init__(self, doc)
        
    def _get_subforums_urls(self):
        return [ (pq(link).text(), pq(link).attr("href") )for link in self("h3.hidden:contains('Sub-forums')").siblings(".bordered-table").eq(0).find("h4 a")]

    def get_subforums(self):
        urls = self._get_subforums_urls()
        print urls

    def _local_cache_exist(self):
        return os.path.exists(self._get_cache_path())
    
    def _get_cache_path(self):
        return os.path.join(webpage_cache_path , sha1(self.url).hexdigest() + ".html")



class SubForumPage(pq):
    def __init__(self,argv,kwargs):
        pq.__init__(self,*argv,**kwargs)
    
    def load_page
    @staticmethod
    def instantiate():


if __name__ == "__main__":
    cfp = CourseForumPage.instantiate()
    cfp.load_page("pgm")
    cfp.get_subforums()

#"""crawl forum page and get subforum info"""
import re
from pyquery import PyQuery as pq
from scrapy.spider import BaseSpider
from scrapy.http import Request
from Cookie import SimpleCookie

from coursera.crawler.req_header import RequestHeader

class ForumSpider(BaseSpider):
    name = "forumtest"
    def __init__(self,course_id):
        self.course_id = course_id
        #self.name = "forum:" + course 
        self.start_urls = ["http://class.coursera.org/design-2012-001/class"]

    def _load_course_url(self):
        return 

    def _load_header(self):
        return RequestHeader(self.course_id,"forum")

    def parse(self,response):
        print response

    def make_requests_from_url(self,url):
        try:
            course_id = re.findall(r'class.coursera.org/(.*)/class',url)[0]
        except IndexError:
            print "unrecognizable coursera course URL, because course id cannot be extracted"
            return 
        forum_url = "http://class.coursera.org/%s/forum/index" %course_id
        print forum_url
        headers = self._load_header()
        cookie_string = headers["Cookie"]
        del headers["Cookie"]
        cookie = SimpleCookie(cookie_string)
        print headers
        print cookie.keys()
        return Request(forum_url, headers = headers, cookies = cookie)

if __name__ == "__main__":
    pass

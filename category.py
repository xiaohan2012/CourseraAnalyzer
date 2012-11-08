from nltk import ConditionalFreqDist

from db import db
from course import *

class Category(dict):
    def __init__(self, data):
        dict.__init__(self,data)
        self.courses = None

    def get_courses(self):
        if not self.courses:
            self.courses = map(Course, db.courses.find({"_id":{"$in":self["courses"]}}) )
        return self.courses            
    
    def get_top_univs(self,n = None):
        """ the university in whose courses this category occurs most often"""
        univs = Categories.get_cat2univ_stat()[self["short_name"]]
        if n is None:
            return univs.items()[:] 
        else:        
            return univs.items()[:n] 
            

class Categories(list):
    cat2univ_stat = None

    def __init__(self,data):
        list.__init__(self,data)

    @staticmethod
    def get(criteria = {}):
        return Categories(map(Category, 
                   list(db.categories.find(criteria))))
    @staticmethod    
    def get_cat2univ_stat():
        if not Categories.cat2univ_stat:
             Categories.cat2univ_stat = ConditionalFreqDist((cat["short_name"],u["short_name"]) 
                                            for cat in Categories.get()
                                                for c in cat.get_courses()
                                                    for u in c.get_univs())
        return Categories.cat2univ_stat


    def order_by_course_count(self,reverse = True):
        list.__init__(self,Categories(sorted(self,key = lambda c:len(c.get_courses()),reverse = reverse)))
    


if __name__ == "__main__":
    cats = Categories.get()
    cats.order_by_course_count()

    for cat in cats:
        cs = cat.get_courses()
        print cat["name"] , len(cs)
        print cat.get_top_univs(3)
        print 

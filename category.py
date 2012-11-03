from db import db
from course import *

class Category(dict):
    def __init__(self, data):
        dict.__init__(self,data)
        self.courses = None

    def get_courses(self):
        if not self.courses:
            print len(self["courses"])
            self.courses = map(Course, db.courses.find({"_id":{"$in":self["courses"]}}) )
        return self.courses            


class Categories(list):
    def __init__(self,data):
        list.__init__(self,data)

    @staticmethod
    def get(criteria = {}):
        return Categories(map(Category, 
                   list(db.categories.find(criteria))))

if __name__ == "__main__":
    cats = Categories.get()
    for cat in cats:
        cs = cat.get_courses()
        print len(cs)

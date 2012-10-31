from db import db
from pprint import pprint

class Course(dict):
    def __init__(self,data):
        dict.__init__(self,data)

    def get_instructor(self,data):
        return self["instructor"]
    
class Courses(object):
    @staticmethod
    def get(criteria):
        print criteria
        return map(Course , 
                   list(db.courses.find(criteria)))

if __name__ == "__main__":
    courses = Courses.get({"university-ids":{"$all":["stanford"]}})
    print len(courses)
    pprint(courses[0])


from db import db
from course import Courses

def get_all_univs():
    univs = []
    for u in db.univs.find():
        univs.append(University(u))
    print "found %d univerisies" %len(univs)
    return univs

def get_univ_count():
    return db.univs.find().count()

class University(dict):
    def __init__(self,data):
        dict.__init__(self, data)
        self.courses = None

    def get_courses(self):
        if not self.courses:
            self.courses = Courses.get({"university-ids":{"$all":[self["short_name"]]}})
        return self.courses

class Universities(list):
    def __init__(self,data):
        list.__init__(self,data)
    
    @staticmethod
    def get(criteria = {}):
        return Universities(map(University, 
                   list(db.univs.find(criteria))))

    def sort_by_course_count(self,reverse = True):
        list.__init__(self,Universities(sorted(self,key = lambda u:len(u.get_courses()),reverse = reverse)))
    
    #sort by category?
    #cluster by category?

    def __repr__(self):
        return "\t".join(map(lambda c:c["name"], self))


if __name__ == "__main__":
    univs = Universities.get()
    univs.sort_by_course_count()

    for u in univs[:5]:
        print "%-12s from %10s:%d" %(u["name"] , u["short_name"] , len(u.get_courses()) )

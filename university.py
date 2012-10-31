from db import db
from courses import Courses

def get_all_univs():
    univs = []
    for u in db.univs.find():
        univs.append(University(u))
    print "found %d univerisies" %len(univs)
    return univs

class University(dict):
    def __init__(self,data):
        dict.__init__(self, data)
        self.courses = None

    def get_courses(self):
        if not self.courses:
            self.courses = Courses.get({"university-ids":{"$all":[self["short_name"]]}})
        return self.courses

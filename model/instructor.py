from db import db
from course import Courses

class Instructor(dict):
    def __init__(self,data):
        dict.__init__(self, data)
        self.courses = None

    def get_courses(self):
        if not self.courses:
            return Courses.get({"instructor":self["name"]})
        return self.courses

class Instructors(list):
    def __init__(self,data):
        list.__init__(self,data)
    
    @staticmethod
    def get(criteria = {}):
        return Instructors(map(Instructor, 
                   list(db.instructors.find(criteria))))

    def sort_by_course_count(self,reverse = True):
        list.__init__(self,Instructors(sorted(self,key = lambda u:len(u.get_courses()),reverse = reverse)))

if __name__ == "__main__":
    ins = Instructors.get()
    ins.sort_by_course_count()

    for i in ins:
        print "%-12s:%d" %(i["name"] , len(i.get_courses()) )


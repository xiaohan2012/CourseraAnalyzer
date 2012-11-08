from db import db

class Course(dict):
    def __init__(self,data):
        dict.__init__(self,data)

    def get_instructor(self):
        return self["instructor"]

    def get_cats(self):
        "get course categories"
        return self["categories"]

    def get_univs(self):
        return self["universities"]

class Courses(list):
    def __init__(self,data):
        list.__init__(self,data)

    @staticmethod
    def get(criteria):
        #here is the cool part
        return Courses(map(Course , 
                   list(db.courses.find(criteria))))

    def __repr__(self):
        return "\t".join(map(lambda c:c["name"], self))

if __name__ == "__main__":
    courses = Courses.get({"university-ids":{"$all":["stanford"]}})
    print courses
    print len(courses)

    from pprint import pprint
    pprint(courses[0])


from db import db

class Courses(object):
    def __init__(self):
        self.data = db.courses

    def filter_by(self,criteria):
        print criteria
        return list(self.data.find(criteria))

if __name__ == "__main__":
    cs = Courses()
    print len(cs.filter_by({"university-ids":{"$all":["stanford"]}}))


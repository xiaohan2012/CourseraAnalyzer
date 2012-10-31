from simplejson import load
from codecs import open

from db import db

def gen_courses_to_db(path = "data/courses.js"):
    data = load(open(path,"r","utf8"))
    for c in data:
        db.courses.update({"id":c["id"]},c,True)
    print "write in %d courses" %db.courses.find().count()

def gen_univs_to_db(path = "data/univs.js"):
    data = load(open(path,"r","utf8"))
    for c in data:
        db.univs.update({"id":c["id"]},c,True)
    print "write in %d univs" %db.univs.find().count()

def gen_instructors_to_db():
    for c in db.courses.find():
        db.instructors.update({"name":c["instructor"]},c,True)
    print "write in %d instructors" %db.instructors.find().count()


if __name__ == "__main__":
    #gen_courses_to_db()
    #gen_univs_to_db()
    gen_instructors_to_db()

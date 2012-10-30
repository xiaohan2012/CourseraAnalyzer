from simplejson import load
from codecs import open

from db import db

def write_courses_to_db(path = "data/courses.js"):
    data = load(open(path,"r","utf8"))
    for c in data:
        db.courses.update({"id":c["id"]},c,True)
    print "write in %d records" %db.courses.find().count()

if __name__ == "__main__":
    write_courses_to_db()

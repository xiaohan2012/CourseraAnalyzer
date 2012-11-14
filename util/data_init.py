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
        db.instructors.update({"name":c["instructor"]},{"name":c["instructor"],"univ_short_name":c["universities"][0]["short_name"]},True)
    print "write in %d instructors" %db.instructors.find().count()

def gen_categories_to_db():
    for c in db.courses.find():
        for cat in c["categories"]:
            if not db.categories.find({"id":cat["id"]}).count():#exists
                cat.update({"courses":[]})
                db.categories.update({"id":cat["id"]},cat,True)#upsert it
            else:                
                db.categories.update({"id":cat["id"]},{"$addToSet":{"courses":c["_id"]}})#add course
    print "write in %d categories" %db.categories.find().count()            

if __name__ == "__main__":
    #gen_courses_to_db()
    #gen_univs_to_db()
    #gen_instructors_to_db()
    gen_categories_to_db()

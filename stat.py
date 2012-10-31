import numpy as np

from university import get_all_univs

from db import db

def get_univ_count():
    return db.univs.find().count()

def get_instructor_count():
    return db.instructors.find().count()

def univ_sort_by_course_count(reverse = True):
    pass

if __name__ == "__main__":
    univs = get_all_univs()
    print len(univs)
    univs = sorted(univs,key = lambda u:len(u.get_courses()),reverse = True)

    for u in univs:
        print "%-12s:%d" %(u["short_name"] , len(u.get_courses()) )

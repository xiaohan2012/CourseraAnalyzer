import numpy as np

from university import *
from instructor import *
from course import *

from db import db

def all_univs_sort_by_course_count(reverse = True):
    return sorted(get_all_univs(),key = lambda u:len(u.get_courses()),reverse = reverse)

def all_instructors_sort_by_course_count(reverse = True):
    return sorted(get_all_instructors(),key = lambda i:len(i.get_courses()),reverse = reverse)

if __name__ == "__main__":
    #univs = all_univs_sort_by_course_count()
    #for u in univs:
        #print "%-12s:%d" %(u["short_name"] , len(u.get_courses()) )

    ins = all_instructors_sort_by_course_count()
    for i in ins[:5]:
        print "%-12s from %10s:%d" %(i["name"] , i["univ_short_name"] , len(i.get_courses()) )


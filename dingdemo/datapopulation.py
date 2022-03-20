import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
     'dingdemo.settings')

import datetime
import django

django.setup()

from dingapp.models import Course, Student

def populate():
    # First, we will create lists of students containing the pages
    # we want to add into each course.
    # Then we will create a dictionary of dictionaries for our courses.
    # This might seem a little bit confusing, but it allows us to iterate
    # through each data structure, and add the data to our models.

    was_students = [
    {'name': 'Aiden',
    'dob': datetime.date(2000, 7, 3),
    'url':'http://www.google.com'},
    {'name':'Ashley',
    'dob': datetime.date(2002, 1, 3),
        'url':'http://www.google.com'},
    ]

    se_students = [
    {'name': 'Finley',
    'dob': datetime.date(1999, 8, 3),
        'url':'http://www.google.com'},
    {'name':'James',
    'dob': datetime.date(2001, 3, 10),
     'url':'http://www.google.com'},
    ]


    courses = {'Web Application Systems': {'students': was_students},
    'Software Engineering': {'students': se_students},}



    # If you want to add more courses or students,
    # add them to the dictionaries above.

    # The code below goes through the course dictionary, then adds each course,
    # and then adds all the associated students for that course.
    for cname, cdata in courses.items():
        c = add_course(cname)
        for s in cdata['students']:
            add_student(c, s['name'], s['dob'],s['url'])


def add_student(course, name, br, url):
        s = Student.objects.get_or_create(course=course, name=name, dateofbirth=br)[0]
        #s.dateofbirth = br
        s.url=url
        s.save()
        return s

def add_course(name):
        c = Course.objects.get_or_create(name=name)[0]
        c.save()
        return c

if __name__ == '__main__':
    print('Starting dingapp population script...')
    populate()

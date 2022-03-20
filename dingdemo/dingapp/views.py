from django.shortcuts import render
from django.http import HttpResponse
from dingapp.models import Course
from dingapp.models import Student


# Create your views here.

def index(request):
    course_list = Course.objects.all()

    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['courses'] = course_list
    
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage matches to {{ boldmessage }} in the template!
    #context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'dingapp/index.html', context=context_dict)
    #return HttpResponse("Congratulations!");

def show_course(request, course_name_slug):
    context_dict = {}
    try:
        course = Course.objects.get(slug=course_name_slug)
        students = Student.objects.filter(course=course)
        context_dict['students'] = students
        context_dict['course'] = course
    except Course.DoesNotExist:
        context_dict['course'] = None
        context_dict['students'] = None
    return render(request, 'dingapp/course.html', context=context_dict)

def about(request):
    return HttpResponse("This page is to demonstrate Django application development!");

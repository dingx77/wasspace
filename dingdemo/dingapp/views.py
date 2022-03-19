from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage matches to {{ boldmessage }} in the template!
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'dingapp/index.html', context=context_dict)
    #return HttpResponse("Congratulations!");

def about(request):
    return HttpResponse("This page is to demonstrate Django application development!");

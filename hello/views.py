import re
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

# TEST URLS
#TODO Remove before ship
print('http://127.0.0.1:8000/hello/Kimberly')
# END TEST URLS

# Create your views here.
def home(request):
    return HttpResponse("Hello, Django!")

def hello_there(request, name):
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )
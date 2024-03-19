from django.shortcuts import render
from django.http  import HttpResponse


# Create your views here.
rooms=[
    {'id':1, 'name':'lets learn python!'},
    {'id':1, 'name':'design with me'},
    {'id':1, 'name':'frontend developer'},
]


def home(request):
    #return HttpResponse ("Home Page") 
    # return  render (request, 'home.html')
     return  render (request, 'home.html', {'rooms': rooms})


def room(request):
    #return HttpResponse ("ROOM") 
    return  render (request,'room.html')
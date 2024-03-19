from django.shortcuts import render
from django.http  import HttpResponse


# Create your views here.
rooms=[
    {'id':1, 'name':'lets learn python!'},
    {'id':2, 'name':'design with me'},
    {'id':3, 'name':'frontend developer'},
]


def home(request):
    #return HttpResponse ("Home Page") 
    # return  render (request, 'home.html')
    # return  render (request, 'home.html', {'rooms': rooms})
    context = {'rooms': rooms}
    # return  render (request, 'home.html', context)
    return  render (request, 'base/home.html', context)

def room(request,pk):
    #return HttpResponse ("ROOM") 
    #return  render (request,'room.html')
    return  render (request,'base/room.html')

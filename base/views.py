from django.shortcuts import render, redirect
from django.http  import HttpResponse
from .models import Room
from .forms import RoomForm


# Create your views here.
# rooms=[
#     {'id':1, 'name':'lets learn python!'},
#     {'id':2, 'name':'design with me'},
#     {'id':3, 'name':'frontend developer'},
# ]


def home(request):
    #return HttpResponse ("Home Page") 
    # return  render (request, 'home.html')
    # return  render (request, 'home.html', {'rooms': rooms})
    rooms=Room.objects.all()    
    context = {'rooms': rooms}
    # return  render (request, 'home.html', context)
    return  render (request, 'base/home.html', context)

def room(request,pk):
    #return HttpResponse ("ROOM") 
    #return  render (request,'room.html')
    # room = None
    # for i in rooms:
    #     if i['id'] == int(pk):
    #         room=i
    room=Room.objects.get(id=pk)  
    context = {'room': room}        
    #return  render (request,'base/room.html')
    return  render (request,'base/room.html', context)


def createRoom(request):
     form=RoomForm()
     if request.method=='POST':
        # print(request.POST)
        form=RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

     context={'form':form}
     return  render (request,'base/room_form.html', context)



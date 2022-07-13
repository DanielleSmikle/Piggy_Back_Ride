from django.shortcuts import render
from .models import Room, Scholar, Parent

# Create your views here.

def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'piggy/room_list.html', {'rooms':rooms})

def scholar_list(request):
    scholars = Scholar.objects.all()
    return render(request, 'piggy/scholar_list.html', {'scholars': scholars})

def parent_list(request):
    parents = Parent.objects.all()
    return render(request, 'piggy/parent_list.html', {'parents': parents})

def room_detail(request, pk):
    room = Room.objects.get(id=pk)
    return render( request, 'piggy/room_detail.html', {'room':room})

def scholar_detail(request, pk):
    scholar = Scholar.objects.get(id=pk)
    return render( request, 'piggy/scholar_detail.html', {'scholar':scholar})

def parent_detail(request, pk):
    parent = Parent.objects.get(id=pk)
    return render( request, 'piggy/parent_detail.html', {'parent':parent})

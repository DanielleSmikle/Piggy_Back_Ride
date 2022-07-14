from django.shortcuts import render, redirect

from piggy.forms import RoomForm
from .models import Room, Scholar, Parent
from .forms import ParentForm, Room, Scholar, Parent, ScholarForm

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




def room_create(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save()
            return redirect('room_detail', pk= room.pk)

    else:
        form = RoomForm()
    return render(request, 'piggy/room_form.html', {'form':form})

def scholar_create(request):
    if request.method == 'POST':
        form = ScholarForm(request.POST)
        if form.is_valid():
            scholar = form.save()
            return redirect('scholar_detail', pk= scholar.pk)

    else:
        form = ScholarForm()
    return render(request, 'piggy/scholar_form.html', {'form':form})

def parent_create(request):
    if request.method == 'POST':
        form = ParentForm(request.POST)
        if form.is_valid():
            parent = form.save()
            return redirect('parent_detail', pk= parent.pk)

    else:
        form = ParentForm()
    return render(request, 'piggy/parent_form.html', {'form':form})

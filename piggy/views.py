from django.shortcuts import render, redirect
from django.http import JsonResponse


# from piggy.forms import RoomForm
from .models import Room, Scholar, Parent
from .forms import ParentForm, Room, Scholar, Parent, ScholarForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from rest_framework import generics
from .serializers import RoomSerializer, ScholarSerializer, ParentSerializer


# Create your views here.

class RoomList(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class RoomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class= RoomSerializer

class ScholarList(generics.ListCreateAPIView):
    queryset = Scholar.objects.all()
    serializer_class = ScholarSerializer

class ScholarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Scholar.objects.all()
    serializer_class= ScholarSerializer

class ParentList(generics.ListCreateAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer

class ParentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Parent.objects.all()
    serializer_class= ParentSerializer






class RoomCreate(CreateView):
    model = Room
    fields = ['room_number','teacher_Name','scholar_Name', 'photo_url']
    template_name = 'piggy/room_form.html'
    success_url= '/rooms/'

class RoomUpdate(UpdateView):
    model = Room
    fields = ['room_number','teacher_Name','scholar_Name', 'photo_url']
    template_name = 'piggy/room_update_form.html'
    success_url= '/rooms/'

class RoomDelete(DeleteView):
    model = Room
    template_name = 'piggy/room_delete_form.html'
    success_url= '/rooms/'

class ScholarCreate(CreateView):
    model = Scholar
    fields = ['scholar_name', 'photo_url', 'parent_Name', 'date_Of_Birth', 'teacher_Name', 'grade_Level','room_Number','pickup_Method']
    template_name = 'piggy/scholar_form.html'

class ScholarUpdate(UpdateView):
    model = Scholar
    fields = ['scholar_name', 'photo_url', 'parent_Name', 'date_Of_Birth', 'teacher_Name', 'grade_Level','room_Number','pickup_Method']
    template_name = 'piggy/scholar_update_form.html'
    success_url= '/scholars/'

class ScholarDelete(DeleteView):
    model = Scholar
    template_name = 'piggy/scholar_delete_form.html'
    success_url= '/scholars/'

class ParentCreate(CreateView):
    model = Parent
    fields = ['first_name','last_name', 'relation_To_Scholar', 'scholar', 'phone_number']
    template_name = 'piggy/parent_form.html'
    success_url= '/parents/'

class ParentUpdate(UpdateView):
    model = Parent
    fields = ['first_name','last_name', 'relation_To_Scholar', 'scholar', 'phone_number']
    template_name = 'piggy/parent_update_form.html'
    success_url= '/parents/'

class ParentDelete(DeleteView):
    model = Parent
    template_name = 'piggy/parent_delete_form.html'
    success_url= '/parents/'

def room_list(request):

    rooms = Room.objects.all()
    values_rooms = rooms.values('room_number', 'teacher_Name','scholar_Name','photo_url')
    list_rooms = list(values_rooms)
    
    print(type(rooms))
    print(type(values_rooms))
    print(type(list_rooms))


    return JsonResponse(list_rooms, safe=False)
    # return render(request, 'piggy/room_list.html', {'rooms':rooms})

def scholar_list(request):
    
    scholars = Scholar.objects.all()
    values_scholars = scholars.values('scholar_name','photo_url','parent_Name','date_Of_Birth','teacher_Name','grade_Level','room_Number','pickup_Method')
    list_scholars = list(values_scholars)

    print(type(scholars))
    print(type(values_scholars))
    print(type(list_scholars))

    return JsonResponse(list_scholars, safe =False)
    # return render(request, 'piggy/scholar_list.html', {'scholars': scholars})

def parent_list(request):
    parents = Parent.objects.all()
    values_parents = parents.values('first_name','last_name','relation_To_Scholar','scholar','phone_number')
    list_parents = list(values_parents)

    print(type(parents))
    print(type(values_parents))
    print(type(list_parents))

    return JsonResponse(list_parents, safe=False)
    # return render(request, 'piggy/parent_list.html', {'parents': parents})

def room_detail(request, pk):
    room = Room.objects.get(id=pk)
    return render( request, 'piggy/room_detail.html', {'room':room})

def scholar_detail(request, pk):
    scholar = Scholar.objects.get(id=pk)
    return render( request, 'piggy/scholar_detail.html', {'scholar':scholar})

def parent_detail(request, pk):
    parent = Parent.objects.get(id=pk)
    return render( request, 'piggy/parent_detail.html', {'parent':parent})




# def room_create(request):
#     if request.method == 'POST':
#         form = RoomForm(request.POST)
#         if form.is_valid():
#             room = form.save()
#             return redirect('room_detail', pk= room.pk)

#     else:
#         form = RoomForm()
#     return render(request, 'piggy/room_form.html', {'form':form})

# def scholar_create(request):
#     if request.method == 'POST':
#         form = ScholarForm(request.POST)
#         if form.is_valid():
#             scholar = form.save()
#             return redirect('scholar_detail', pk= scholar.pk)

#     else:
#         form = ScholarForm()
#     return render(request, 'piggy/scholar_form.html', {'form':form})

# def parent_create(request):
#     if request.method == 'POST':
#         form = ParentForm(request.POST)
#         if form.is_valid():
#             parent = form.save()
#             return redirect('parent_detail', pk= parent.pk)

#     else:
#         form = ParentForm()
#     return render(request, 'piggy/parent_form.html', {'form':form})

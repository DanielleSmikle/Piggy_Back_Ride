from django.shortcuts import render, redirect

# from piggy.forms import RoomForm
from .models import Room, Scholar, Parent
from .forms import ParentForm, Room, Scholar, Parent, ScholarForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import View
# at top of file with other imports
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Auth
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator




# Create your views here.

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
    success_url = '/scholars/'

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
    fields = ['first_name','last_name', 'relation_To_Scholar', 'phone_number']
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

@login_required
def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'piggy/room_list.html', {'rooms':rooms})

@login_required
def scholar_list(request):
    scholars = Scholar.objects.all()
    return render(request, 'piggy/scholar_list.html', {'scholars': scholars})

def parent_list(request):
    parents = Parent.objects.all()
    print(parents)
    return render(request, 'piggy/parent_list.html', {'parents': parents})
    
@login_required
def room_detail(request, pk):
    room = Room.objects.get(id=pk)
    return render( request, 'piggy/room_detail.html', {'room':room})

@login_required
def scholar_detail(request, pk):
    scholar = Scholar.objects.get(id=pk)
    return render( request, 'piggy/scholar_detail.html', {'scholar':scholar})

@login_required
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


class Signup(View):
    # show a form to fill out
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    # on form submit, validate the form and login the user.
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("artist_list")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)


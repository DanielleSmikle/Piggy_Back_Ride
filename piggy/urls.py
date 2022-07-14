from django.urls import path
from . import views


urlpatterns = [
    path('rooms', views.room_list, name='room_list'),
    path('rooms/<int:pk>', views.room_detail, name='room_detail'),
    path('rooms/new', views.room_create, name='room_create'),
   
    path('scholars', views.scholar_list, name='scholar_list'),
    path('scholars/<int:pk>', views.scholar_detail, name='scholar_detail'),
    path('scholars/new', views.scholar_create, name='scholar_create'),

    path('parents', views.parent_list, name='parent_list'),
    path('parents/<int:pk>', views.parent_detail, name='parent_detail'),
    path('parents/new', views.parent_create, name='parent_create'),
    
]
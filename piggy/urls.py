from django.urls import path
from . import views


urlpatterns = [
    path('', views.room_list, name='room_list'),
    path('rooms/<int:pk>', views.room_detail, name='room_detail'),
    path('scholars', views.scholar_list, name='scholar_list'),
    path('parents', views.parent_list, name='parent_list')
 
]
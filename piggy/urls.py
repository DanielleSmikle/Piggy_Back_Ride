from django.urls import path
from . import views


urlpatterns = [
    path('', views.room_list, name='room_list'),
    path('rooms/<int:pk>', views.room_detail, name='room_detail'),
   
    path('scholars', views.scholar_list, name='scholar_list'),
    path('scholars/<int:pk>', views.scholar_detail, name='scholar_detail'),

    path('parents', views.parent_list, name='parent_list'),
    path('parents/<int:pk>', views.parent_detail, name='parent_detail'),
    
]
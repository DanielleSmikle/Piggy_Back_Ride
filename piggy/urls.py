from django.urls import path
from . import views


urlpatterns = [
    path('rooms/', views.room_list, name='room_list'),
    path('rooms/<int:pk>', views.room_detail, name='room_detail'),
    # path('rooms/new', views.room_create, name='room_create'),
    path('rooms/new', views.RoomCreate.as_view(), name='room_create'),
    path('rooms/<int:pk>/update', views.RoomUpdate.as_view(), name='room_update'),
    path('rooms/<int:pk>/delete', views.RoomDelete.as_view(), name='room_delete'),
   
    path('scholars/', views.scholar_list, name='scholar_list'),
    path('scholars/<int:pk>', views.scholar_detail, name='scholar_detail'),
    # path('scholars/new', views.scholar_create, name='scholar_create'),
    path('scholars/new', views.ScholarCreate.as_view(), name='scholar_create'),
    path('scholars/<int:pk>/update', views.ScholarUpdate.as_view(), name='scholar_update'),
    path('scholars/<int:pk>/delete', views.ScholarDelete.as_view(), name='scholar_delete'),

    path('parents/', views.parent_list, name='parent_list'),
    path('parents/<int:pk>', views.parent_detail, name='parent_detail'),
    # path('parents/new', views.parent_create, name='parent_create'),
    path('parents/new', views.ParentCreate.as_view(), name='parent_create'),
    path('parents/<int:pk>/update', views.ParentUpdate.as_view(), name='parent_update'),
    path('parents/<int:pk>/delete', views.ParentDelete.as_view(), name='parent_delete'),
    
]
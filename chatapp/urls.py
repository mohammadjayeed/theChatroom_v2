from django.urls import path,include
from . import views
urlpatterns = [
   
    path('', views.index,name='rooms'),
    path('<slug:slug>/', views.chatroom,name='chatroom'),

]
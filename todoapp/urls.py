from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.signup, name='signup'),
    path('loginn/', views.loginn, name='loginn'),
    path('todo/', views.todo, name='todo'),
    path('logoutt/', views.logoutt, name='logoutt'),
    path('addtask/', views.add_task, name='add_task'),
]

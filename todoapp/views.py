from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import TODO
from . import models
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        emailid = request.POST.get('email')
        password = request.POST.get('password')
        print(username,emailid,password)
        my_user = User.objects.create_user(username,emailid,password)
        my_user.save()
        print(username,emailid,password)
        return redirect('/loginn')
    else:
        return render(request, "signup.html")
    
def loginn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/todo')
        else:
            print("Invalid credentials")
            return redirect('/')
    return render(request, 'loginn.html')
        
def todo(request):  
    if request.method == 'POST':
        title = request.POST.get('title')
        print(title)
        if request.user.is_authenticated:
            obj = TODO(title=title, user=request.user)
            obj.save()
            print("Task added:", title)
        else:
            return redirect('/loginn')
    tasks = TODO.objects.filter(user=request.user)
    return render(request, "todo.html",{"tasks": tasks})

def logoutt(request):
    logout(request)
    return redirect('/loginn')

def add_task(request):
    # views.py
    if request.method == 'POST':
        task = request.POST.get('task')
        if task and request.user.is_authenticated:
            TODO.objects.create(title=task, user=request.user)  # Adjust field name
        return redirect('/todo')

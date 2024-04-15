from django.shortcuts import render
from django.http import HttpResponse

# request handling

def show_home(request):
    return render(request, 'home.html')

def show_instructor_list(request):
    return render(request, 'instructor_list.html')

def show_register(request):
    return render(request, 'register.html')

def show_login(request):
    return render(request, 'login.html')
from django.shortcuts import render
from .models import todo

def home(request):
    todos = todo.objects.all
    return render(request, 'home.html',{'todos': todos})

def about(request):
    return render(request, 'about.html', {'name': 'Marcus'})
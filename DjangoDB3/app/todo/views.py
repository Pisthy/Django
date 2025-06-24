from django.shortcuts import render, redirect, get_object_or_404
from .models import todo 
from .forms import TodoForm 

def home(request):
    todos = todo.objects.all() 
    return render(request, 'home.html', {'todos': todos})

def about(request):
    return render(request, 'about.html', {'name': 'Marcus'})

def update(request):
    return render(request, 'update.html' )

def update_todo(request, id):
    tarefa = get_object_or_404(todo, id=id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TodoForm(instance=tarefa)
    return render(request, 'update.html', {'form': form})

def delete_todo(request, id):
    tarefa = get_object_or_404(todo, id=id)
    tarefa.delete()
    return redirect('home')

def adicionar(request):
    return render(request, 'adicionar.html')

def adicionar_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TodoForm()
    return render(request, 'adicionar.html', {'form': form})

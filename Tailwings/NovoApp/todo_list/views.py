from django.shortcuts import render
from .models import todo
# Create your views here.
def home(request):
    todos = todo.objects.all()
    return render(request, 'home.html', {'todos': todos})

def about(request):
    context = {'name': 'Marcus Vinicius', 'age': 23}
    return render(request, 'about.html', context)
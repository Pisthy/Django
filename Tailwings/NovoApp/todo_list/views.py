from django.shortcuts import render
from .models import todo
from .forms import TodoForm

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = TodoForm(request.POST or Nome)
        if form.is_valid():
            form.save()
            todos = todo.objects.all()
            return render(request, 'home.html', {'todos': todos})

def about(request):
    context = {'name': 'Marcus Vinicius', 'age': 23}
    return render(request, 'about.html', context)
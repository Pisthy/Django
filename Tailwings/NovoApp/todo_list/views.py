from django.shortcuts import render
from .models import todo
from .forms import TodoForm

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
    todos = todo.objects.all()
    form = TodoForm()
    return render(request, 'home.html', {'todos': todos, 'form': form})

def about(request):
    context = {'name': 'Marcus Vinicius', 'age': 23}
    return render(request, 'about.html', context)
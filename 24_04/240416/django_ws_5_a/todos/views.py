from django.shortcuts import render
from .models import Todo

# Create your views here.
def index(request):
    # todos로 Todo model을 쓰는 데이터 전부를 받는다.
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'todos/index.html', context)

def create_todo(request):
    return render(request, 'todos/create_todo.html')

def detail(request, pk):
    # todos - todo 관계로 특정 하나 데이터를 설정함
    todo = Todo.objects.get(pk=pk)
    context = {
        'todo': todo
    }
    return render(request, 'todos/detail.html', context)
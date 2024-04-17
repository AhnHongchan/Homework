from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    todo_list = Todo.objects.all()
    context = {
        'todo_list': todo_list
    }
    return render(request, 'todos/index.html', context)

def create_todo(request):
    return render(request, 'todos/create_todo.html')

def detail(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    context = {
        'todo': todo
    }
    return render(request, 'todos/detail.html', context)

def new_todo(request):
    work = request.POST.get('work')
    content = request.POST.get('content')
    is_completed = False

    todo = Todo(work=work, content=content, is_completed=is_completed)
    todo.save()
    return redirect('todos:detail', todo.pk)

def delete_todo(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    todo.delete()
    return redirect('todos:index')

# url에 <int:todo_pk>라고 적었기 때문에
# url 패턴에서 정의한 경로 변수와 뷰 함수의 매개변수의 이름이 일치해야 한다.
def update_todo(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    context = {
        'todo': todo,
    }
    return render(request, 'todos/update.html', context)

def edit_todo(request, todo_pk):
    todo = Todo.objects.get(pk = todo_pk)
    todo.work = request.POST.get('work')
    todo.content = request.POST.get('content')
    todo.save()
    # detail 이름 가진 url로 다시 연결시켜달라
    return redirect('todos:detail', todo.pk)


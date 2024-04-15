from django.db import models

# Create your models here.
class Todo(models.Model):
    work = models.CharField(max_length=100)
    content = models.TextField()
    is_completed = models.BooleanField()
    # created_at 생성
    # DateTimeField를 통해 날짜나 시간을 입력할 수 있으며
    # auto_now_add는 생성 시점의 시간을 자동으로 추가한다.
    # Accept the default 'timezone.now'
    created_at = models.DateTimeField(auto_now_add = True)

'''
In [1]: todo = Todo()

In [2]: todo.work = '첫 번째 할 일'

In [3]: todo.content = '상세 내용 1'

In [4]: todo.is_completed = False

In [5]: todo.save()

In [6]: Todo.objects.all()
Out[6]: <QuerySet [<Todo: Todo object (1)>]>

In [7]: todo = Todo()

In [8]: todo.work = '두 번째 할 일'

In [9]: todo.content = '상세 내용 2'

In [10]: todo.is_completed = False

In [11]: todo.save()

In [12]: Todo.objects.all()
Out[12]: <QuerySet [<Todo: Todo object (1)>, <Todo: Todo object (2)>]>

'''

'''
데이터 삭제
In [13]: todo = Todo.objects.get(pk=1)

In [14]: todo.delete()
Out[14]: (1, {'todos.Todo': 1})

In [15]: Todo.objects.all()
Out[15]: <QuerySet [<Todo: Todo object (2)>]>
'''
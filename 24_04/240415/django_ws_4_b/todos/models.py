from django.db import models

# Create your models here.
class Todo(models.Model):
    work = models.CharField(max_length=100)
    content = models.TextField()
    is_completed = models.BooleanField()

'''
데이터 생성

In [2]: todo = Todo()

In [3]: todo.work = '첫 번째 할 일'

In [4]: todo.content = '상세 내용 1'

In [6]: todo.is_completed = False

In [7]: todo.save()

In [8]: Todo.objects.all()
Out[8]: <QuerySet [<Todo: Todo object (1)>]>

In [9]: todo = Todo()

In [10]: todo.work = '두 번째 할 일'

In [11]: todo.content = '상세 내용 2'

In [12]: todo.is_completed = False

In [13]: todo.save()

데이터 조회
In [14]: Todo.objects.all()
Out[14]: <QuerySet [<Todo: Todo object (1)>, <Todo: Todo object (2)>]>

In [15]: exit()
'''

'''
데이터 상세 조회
In [2]: todo = Todo.objects.get(pk=1)

In [3]: todo.work
Out[3]: '첫 번째 할 일'

In [4]: todo.content
Out[4]: '상세 내용 1'

In [5]: todo.is_completed
Out[5]: False

데이터 수정
In [6]: todo.work = '수정된 첫 번째 할 일'

In [7]: todo.save()

데이터 확인
python manage.py runserver 이후
http://127.0.0.1:8000/admin 으로 접속하여 로그인 후
데이터 변화 확인
'''
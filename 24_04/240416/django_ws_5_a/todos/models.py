from django.db import models

# Create your models here.
class Todo(models.Model):
    work = models.CharField(max_length=100)
    content = models.TextField()
    is_completed = models.BooleanField()
    created_at = models.DateField(auto_now_add=True)

    # todos_project(1)처럼 생성되는 걸 인스턴스의 이름 변경을 하고 싶은 경우
    def __str__(self):
        return f'{self.pk}번째 할 일'
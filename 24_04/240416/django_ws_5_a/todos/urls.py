from django.urls import path
from . import views


app_name = 'todos'

urlpatterns = [
    path('', views.index, name='index'),
    path('create_todo/', views.create_todo, name='create_todo'),
    # 기존 경로에서 바꾸어 뒤에 데이터의 pk를 붙인다.
    path('<int:pk>/', views.detail, name='detail'),
]
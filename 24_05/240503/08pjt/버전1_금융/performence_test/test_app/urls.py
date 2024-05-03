from django.urls import path
from . import views

urlpatterns = [
    path('', views.Dataset),
    path('null/', views.null),
    path('create/', views.create_dataset),
]


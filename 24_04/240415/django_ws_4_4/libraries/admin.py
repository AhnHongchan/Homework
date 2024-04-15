from django.contrib import admin
from .models import Book

# Register your models here.
admin.site.register(Book)

# admin 계정을 사용해서 관리자 사이트에서 확인하려면
# admin.site.register(model)을 하여 모델을 관리자 페이지에 등록해줘야 한다.
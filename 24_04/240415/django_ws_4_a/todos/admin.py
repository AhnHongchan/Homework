from django.contrib import admin
from .models import Todo

# Register your models here.
admin.site.register(Todo)
# 관리자 페이지(admin site)에서 모델을 관리하기 위해 등록하는 데 사용합니다.
# admin.site.register
# 관리자 페이지에서 해당 모델의 데이터를 볼 수 있고, 필요한 경우 추가, 삭제할 수 있습니다.
# 관리자가 DB를 직접 조작하지 않고도 모델을 편리하게 관리할 수 있도록 도와줍니다.
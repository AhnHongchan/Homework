from django.shortcuts import render

# Create your views here.
# 메인 페이지를 만드는 index라는 이름의 함수를 작성
def index(request):
    # 왜요?
    # render 함수가 그렇게 만들어져 있습니다.
    return render(request, 'todos/index.html')
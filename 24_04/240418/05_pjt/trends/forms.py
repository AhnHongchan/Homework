from django import forms
from django.forms import TextInput
from .models import Keyword

class KeywordModelForm(forms.ModelForm):
    # form class의 설정을 담고 있다.
    # class Meta에 폼의 설정이나 동작에 영향을 주는 데이터를 모아둘 수 있다.
    class Meta:
        # 이 폼이 사용할 모델을 지정한다.
        # models.py의 Keyword 모델 사용
        model = Keyword
        # Keyword 모델 내에 있는 필드 중 사용할 필드를 적는다.
        # 튜플 형태로 필드 이름을 나열하고, 
        # 하나의 필드만 사용할 때에도 쉼표를 꼭 붙여주어야 한다.
        fields = ('name',)
        # widgets은 웹 어플리케이션에서 사용자가 입력한 데이터를 받을 수 있는 HTML 요소들을 의미한다.
        # Django에서는 폼의 필드를 어떻게 보여줄 지 결정하는 요소이다.
        widgets = {
            'name': TextInput
        }
        # 각 필드의 라벨을 지정한다.
        # forms.py를 이용해 label을 지정할 경우
        # 자동으로 키워드':', 옆에 콜론까지 붙여준다.
        # 즉 따로 콜론을 쓸 필요가 없다.(쓰면 2개 출력된다)
        labels = {
            'name': '키워드',
        }
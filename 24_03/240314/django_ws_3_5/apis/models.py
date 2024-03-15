from django.db import models
from django.core.validators import URLValidator, MinLengthValidator,MaxLengthValidator
# validator를 새로 만들어서 정규식으로 글씨 길이를 제한한다.
# url_length_validator = URLValidator(regex=r'^.{15,60}$')
min_length_validator = MinLengthValidator(limit_value=15)
max_length_validator = MaxLengthValidator(limit_value=60)

class APIInfo(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    # 글씨 길이를 검증하는 Validator를 등록한다.
    api_url = models.URLField(validators=[min_length_validator,max_length_validator])
    documentation_url = models.URLField()
    auth_required = models.BooleanField()
    # 기본적으로None이 들어가게끔 만든다.
    additional_info = models.JSONField(default = 'None',blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

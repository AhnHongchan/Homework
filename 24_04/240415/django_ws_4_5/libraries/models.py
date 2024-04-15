from django.db import models
import requests

# Create your models here.
class Book(models.Model):
    isbn = models.CharField(max_length=10)
    author = models.TextField()
    title = models.TextField()
    category_name = models.TextField()
    category_id = models.IntegerField()
    price = models.IntegerField()
    fixed_price = models.BooleanField()
    pub_date = models.DateField()

    @classmethod
    def insert_data(cls):
        # requests.get을 이용해 외부 API에 GET 요청을 보낸다
        # case 1
        response = requests.get('http://www.aladin.co.kr/ttb/api/ItemList.aspx?ttbkey=ttbhha04081429001&QueryType=ItemNewAll&MaxResults=10&start=1&SearchTarget=Book&output=js&Version=20131101')
        # case 2
        # response = requests.get('http://www.aladin.co.kr/ttb/api/ItemList.aspx', params = {'ttbkey': 'ttbhha04081429001', 'QueryType': 'ItemNewAll' ....})
        
        
        # API의 응답을 JSON 형식으로 가져와서 response.json()을 호출하여 파이썬
        # 객체로 변환한다.

        data = response.json()
        items = data.get('item')

        for item in items:
            # print(item)
            # print(item.get('price'))
            book = cls(isbn = item.get('isbn'),author = item.get('author'),title = item.get('title'),
                       category_name = item.get('categoryName'),category_id = item.get('categoryId'),
                       price = item.get('priceSales'),fixed_price = item.get("fixedPrice"),pub_date = item.get("pubDate"))
            book.save()
from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.TextField()
    pubdate = models.DateField()
    price = models.IntegerField()
    adult = models.BooleanField()

'''
데이터 생성
In [1]: book = Book()

In [2]: book.title = '첫 번째 책'

In [3]: book.author = 'author1'

In [4]: book.price = '100'

In [5]: book.adult = False

In [8]: book.pubdate = '2024-01-01'

In [9]: book.save()

In [10]: book = Book()

In [11]: book.title = '두 번째 책'

In [12]: book.author = '작가'

In [13]: book.pubdate = '2024-01-01'

In [14]: book.price = '1010'

In [15]: book.adult = True

In [16]: book.save()

In [17]: book = Book

In [18]: book = Book()

In [19]: book.title = '세 번째 책'

In [20]: book.author = '작가2'

In [21]: book.pubdate = '2024-01-03'

In [22]: book.price = '10101'

In [23]: book.adult = False

In [24]: book.save()


데이터 출력(모두 순회하여 title만 출력하기)
In [25]: books = Book.objects.all()

In [26]: for book in books:
    ...:     print(book.title)
    ...: 
첫 번째 책
두 번째 책
세 번째 책
'''
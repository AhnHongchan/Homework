from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.TextField()
    pubdate = models.DateField()
    price = models.IntegerField()
    adult = models.BooleanField()

'''
In [1]: book = Book()

In [2]: book.title = '홍길동전'

In [3]: book.author = '허균'

In [4]: book.pubdate = '1994-07-25'

In [5]: book.price = '3000'

In [6]: book.adult = False

In [7]: book.save()

In [8]: book2 = Book()

In [9]: book2.title = '난중일기'

In [10]: book2.author = '이순신'

In [11]: book2.pubdate = '2015-01-21'

In [12]: book2.price = '0'

In [13]: book2.adult=True

In [14]: book2.save()

In [15]: book3 = Book()

In [16]: book3.title = '세종실록'

In [17]: book3.author = '이도'

In [18]: book3.pubdate = '1397-05-15'

In [19]: book3.price = '0'

In [20]: book3.adult = False

In [21]: book3.save()

In [22]: Book.objects.all()
Out[22]: <QuerySet [<Book: Book object (1)>, <Book: Book object (2)>, <Book: Book object (3)>]>
In [23]: books = Book.objects.all()

In [24]: for book in books:
    ...:     print(book.title)
    ...:     print(book.author)
    ...:     print(book.pubdate)
    ...:     print(book.price)
    ...:     print(book.adult)
    ...: 
홍길동전
허균
1994-07-25
3000
False
난중일기
이순신
2015-01-21
0
True
세종실록
이도
1397-05-15
0
False

'''
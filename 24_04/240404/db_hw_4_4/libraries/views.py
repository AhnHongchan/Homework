from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST

from libraries.forms import ReviewForm
from .models import Book, Review

# Create your views here.
def index(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'libraries/index.html', context)

def detail(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    review_form = ReviewForm()
    reviews = book.review_set.all()
    context = {
        'book': book,
        'review_form':review_form,
        'reviews':reviews
    }
    return render(request, 'libraries/detail.html', context)

@require_POST
@login_required
def create_review(request,book_pk):
    book = Book.objects.get(pk = book_pk)
    review_form = ReviewForm(request.POST)
    if review_form.is_valid():
        review = review_form.save(commit=False)
        review.book = book
        review.user = request.user
        review.save()
    return redirect('libraries:detail',book.pk)
    
    
@require_POST
@login_required
def delete_review(request,book_pk,review_pk):
    review = Review.objects.get(pk = review_pk)
    if review.user == request.user:
        review.delete()
    return redirect('libraries:detail',book_pk)
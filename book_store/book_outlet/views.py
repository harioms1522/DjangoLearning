from django.shortcuts import render
from . import models
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.db.models import Avg, Min, Max

# Create your views here.
def index(request):
    books = models.Book.objects.filter()
    total = books.count()
    aggregations = books.aggregate(Avg("ratings"), Min("ratings"), Max("ratings"))
    print(total)
    return render(request, "book_outlet/index.html", {"books": books, "count":total, "aggregations": aggregations})

def book_details(request, book_id):
    try:
        book = models.Book.objects.get(pk=book_id)
        return render(request, "book_outlet/book-detail.html", {"book": book} )
    except: 
        raise Http404()
    
def book_details_slug(request, slug):
    book = get_object_or_404(models.Book, slug=slug)
    return render(request, "book_outlet/book-detail.html", {"book": book} )
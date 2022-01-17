from django.shortcuts import render
from .models import Books
from django.http import HttpResponse

def index(request):

    num_books=Books.objects.all().count()
    # num_instances=BooksInstance.objects.all().count()
   

    return render(
        request,
        'index.html',
        context={'num_books':num_books},
    )
    # return HttpResponse("Hello, world. You're at the polls index.")
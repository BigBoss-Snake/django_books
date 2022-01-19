from django.shortcuts import render
from .models import Books
from django.http import HttpResponse
from django.views import generic

class BookListView(generic.ListView):
    model = Books
    context_object_name = 'book_list'
    template_name = 'index.html'


def index(request):

    num_books=Books.objects.all().count()
    # num_instances=BooksInstance.objects.all().count()
   

    return render(
        request,
        'index.html',
        context={'num_books':num_books},
    )
    # return HttpResponse("Hello, world. You're at the polls index.")

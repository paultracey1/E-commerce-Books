from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Book
from rest_framework import viewsets
from .serializers import BookSerializer
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from .forms import BookForm
from django.utils import timezone
from django.db.models import Q
from django.http import HttpResponseForbidden
from django.contrib import messages, auth
from django.contrib.auth.models import User



# Create your views here.
def all_books(request):
    books = Book.objects.filter(published_date__lte=timezone.now()
                                ).order_by('-published_date')
    args = {}
    args.update(csrf(request))
    return render(request, "books.html", {"books": books}, args)

def book_detail(request, id):
    book  = get_object_or_404(Book, pk=id)
    return render(request, "bookdetail.html", {'book': book})

@login_required(login_url='/accounts/login')
def new_book(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.seller = request.user
            book.published_date = timezone.now()
            book.save()
            return redirect(book_detail, book.pk)
    else:
        form = BookForm()
    return render(request, 'bookaddform.html', {'form': form})


def edit_book(request, id):

    book = get_object_or_404(Book, pk=id)

    if book.seller != request.user:
        #return HttpResponseForbidden()
        messages.error(request, "You don't have authorisation to edit that book.")
        return redirect(reverse('books'))

    if request.method == "POST":
      form = BookForm(request.POST, request.FILES, instance=book)
      if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect(book_detail, post.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'bookaddform.html', {'form': form})




def do_search(request):
    books = Book.objects.filter(Q(title__contains=request.GET['q']) | Q(author__contains=request.GET['q']) | Q(genre__contains=request.GET['q'])).order_by('-published_date')
    return render(request, 'books.html', {'books': books})


def seller_books(request, id):
    user = get_object_or_404(User, pk=id)
    books = Book.objects.filter(seller = user).order_by('-published_date')
    args = {}
    args.update(csrf(request))
    return render(request, "books.html", {"books": books}, args)


def genre_books(request, genre):
    genre = get_object_or_404(Book, pk="genre")
    books = Book.objects.filter(genre=genre).order_by('-published_date')
    args = {}
    args.update(csrf(request))
    return render(request, "books.html", {"books": books}, args)



class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
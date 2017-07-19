from django.conf.urls import url
from .views import all_books, book_detail, new_book, edit_book, do_search, seller_books, genre_books, author_books, delete_book

urlpatterns = [
    url(r'^$', all_books, name='books'),
    url(r'^(?P<id>\d+)$', book_detail, name='book_detail'),
    url(r'^add$', new_book, name='new_book'),
    url(r'^(?P<id>\d+)/edit$', edit_book, name='edit_book'),
    url(r'^search/', do_search, name='search'),
    url(r'^sold_by/(?P<id>\d+)', seller_books, name='seller_books'),
    url(r'^genre/(?P<genre>[\w.@+-]+)', genre_books, name='genre_books'),
    url(r'^author/(?P<author>[\w.@+-]+)', author_books, name='author_books'),
    url(r'^(?P<id>\d+)/delete$', delete_book, name='delete_book'),

]
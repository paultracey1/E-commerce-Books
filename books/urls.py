from django.conf.urls import url
from .views import all_books, book_detail, new_book, edit_book, do_search, seller_books, genre_books

urlpatterns = [
    url(r'^$', all_books, name='books'),
    url(r'^(?P<id>\d+)$', book_detail, name='book_detail'),
    url(r'^add$', new_book, name='new_book'),
    url(r'^(?P<id>\d+)/edit$', edit_book, name='edit_book'),
    url(r'^search/', do_search, name='search'),
    url(r'^sold_by/(?P<id>\d+)', seller_books, name='seller_books'),
    url(r'^genre/(?P<genre>[\w.@+-]+)', genre_books, name='genre_books'),

]
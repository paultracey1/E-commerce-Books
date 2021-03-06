from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

class Book(models.Model):

    DRAMA = 'Drama'
    THRILLER = 'Thriller'
    SELF_HELP = 'Self help'
    GENRE = (
        (DRAMA, 'Drama'),
        (THRILLER, 'Thriller'),
        (SELF_HELP, 'Self help'),
    )

    AVAILABLE = 'Available'
    SOLD = 'Sold'
    STATUS = (
        (AVAILABLE, 'Available'),
        (SOLD, 'Sold'),
    )

    seller = models.ForeignKey(User)
    title = models.CharField(max_length=254, default='')
    author = models.CharField(max_length=254, default='')
    genre = models.CharField(max_length=254, choices=GENRE)
    description = models.TextField()
    ISBN = models.CharField(max_length=13, default='')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images', default='images/default.png')
    published_date = models.DateTimeField(blank=True, null=True)

    status = models.CharField(max_length=254, choices=STATUS, default='Available')

    def __str__(self):
        return self.title
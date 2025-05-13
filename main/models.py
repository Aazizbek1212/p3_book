from django.db import models
from django.contrib.auth import get_user_model


class Genre(models.Model):
    name = models.CharField(max_length=200)
    images = models.ImageField(upload_to='media', blank=True, null=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    brith_date = models.DateField()
    country = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='media')

    def __str__(self):
        return self.name


class Book(models.Model):
    COVER_CHOICES = (
        ('hard', 'Qattiq'),
        ('soft', 'Yumshoq'),
    )

    title = models.CharField(max_length=500)
    aouthors = models.ManyToManyField(Author)
    pages = models.IntegerField(default=0)
    genre = models.ManyToManyField(Genre)
    date_published = models.DateField()
    description = models.TextField(blank=True, null=True)
    language = models.CharField(max_length=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=10)
    image = models.ImageField(upload_to='media')
    paper_format = models.CharField(max_length=2)
    cover = models.CharField(choices=COVER_CHOICES, default=COVER_CHOICES[0][0], max_length=4)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title

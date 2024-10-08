from django.db import models
from main.models import Book


class Order(models.Model):
    STATUS_CHOISES = (
        ('new', 'Yangi buyurtma'),
        ('ready', 'Dastavkaga tayyor'),
        ('waiting', 'Yetkazilmoqda'),
        ('delivered', 'Yetkazildi'),
        ('cancelled', 'Bekor qilindi')

    )

    CITIES = (
        ('Viloyatni tanlang', 'Viloyatni tanlang'),
        ('tashkent', 'Toshkent shahar'),
        ('andijon', 'Andijon viloyati'),
        ('buxoro', 'Buxoro viloyati'),
        ('fargona', "Farg'ona viloyati"),
        ('jizzax', 'Jizzax viloyati'),
        ('namangan', 'Namangan viloyati'),
        ('navoiy', 'Navoiy viloyati'),
        ('qashqadaryo', 'Qashqadaryo viloyati'),
        ('qoraqalpogiston', "Qoraqalpog'iston Respublika"),
        ('samarqand', 'Samarqand viloyati'),
        ('sirdaryo', 'Sirdaryo viloyati'),
        ('surxondaryo', 'Surxondaryo viloyati'),
        ('toshkent', 'Toshkent viloyati'),
        ('xorazm', 'Xorazm viloyati')
    )

    name = models.CharField(max_length=500)
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, blank=True, null=True)
    status = models.CharField(max_length=9, choices=STATUS_CHOISES, default=STATUS_CHOISES[0][0])
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=17, choices=CITIES)
    phone_number = models.CharField(max_length=13)
    created_at = models.DateTimeField(auto_created=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

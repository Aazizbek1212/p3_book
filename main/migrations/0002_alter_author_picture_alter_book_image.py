# Generated by Django 5.0.4 on 2024-05-09 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='picture',
            field=models.ImageField(upload_to='media'),
        ),
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
    ]

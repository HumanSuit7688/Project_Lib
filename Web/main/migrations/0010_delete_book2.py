# Generated by Django 5.0.1 on 2024-02-27 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_rename_book_book2'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book2',
        ),
    ]

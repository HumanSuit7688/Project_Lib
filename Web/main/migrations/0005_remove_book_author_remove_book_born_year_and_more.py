# Generated by Django 5.0.1 on 2024-02-27 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_book_amount_alter_book_born_year_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.RemoveField(
            model_name='book',
            name='born_year',
        ),
        migrations.RemoveField(
            model_name='book',
            name='name',
        ),
        migrations.RemoveField(
            model_name='book',
            name='pages',
        ),
        migrations.RemoveField(
            model_name='book',
            name='public_office',
        ),
    ]
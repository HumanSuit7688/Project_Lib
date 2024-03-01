from django.db import models

class Book(models.Model):
    author = models.TextField(default=' ')
    name = models.TextField(default=' ')
    public_office = models.TextField(default=' ')
    born_year = models.TextField(default=' ')
    pages = models.TextField(default=' ')

    def __str__(self):
        return f'{self.author} - {self.name}'




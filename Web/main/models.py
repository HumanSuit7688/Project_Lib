from django.db import models

class Book(models.Model):
    author = models.CharField(max_length=75)
    name = models.CharField(max_length=100, blank=False)
    public_office = models.CharField(max_length=75)
    born_year = models.DateField()
    pages = models.PositiveSmallIntegerField()
    amount = models.PositiveSmallIntegerField()


    def __str__(self):
        return f'{self.author} - {self.name}'

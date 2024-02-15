from django.db import models

class User(models.Model):
    surname = models.CharField(max_length=30, blank=False)
    name = models.CharField(max_length=30, blank=False)
    patronymic = models.CharField(max_length=40)
    grade_c = models.PositiveSmallIntegerField(blank=False)
    grade_b = models.CharField(max_length=5, blank=False)
    email = models.EmailField(blank=False)
    password = models.TextField(blank=False)

    def __str__(self):
        return f'{self.surname} {self.name}'
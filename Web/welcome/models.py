from django.db import models

class User(models.Model):
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=40)
    grade_c = models.PositiveSmallIntegerField()
    grade_b = models.CharField(max_length=5)
    email = models.EmailField()
    password = models.TextField()
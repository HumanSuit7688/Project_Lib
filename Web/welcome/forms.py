from django import forms
from django.contrib.auth.forms import UserChangeForm

class Log_in_Form(forms.Form):
    login = forms.CharField()

    password = forms.CharField()


class Sign_up_Form(forms.Form):
    Surname = forms.CharField(label='Фамилия')
    Name = forms.CharField(label= 'Имя')
    Patronymic = forms.CharField(label='Отчество')
    Grade_c = forms.ChoiceField(label='Класс (цифра)', choices=((None, None), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11)), initial='')
    Grade_b = forms.ChoiceField(label='Класс (буква)', choices=((None, None), ("А", "А"), ("Б", "Б"), ("В", "В"), ("Г", "Г")), initial='')
    Email = forms.EmailField(label='E-mail')
    Password = forms.CharField(label='Пароль')
    Pssword2 = forms.CharField(label='Пароль (ещё раз)')

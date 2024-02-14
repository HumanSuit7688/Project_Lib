from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .forms import Log_in_Form, Sign_up_Form


def welcome(request):
    redirect_about = reverse("info-type", args=['about'])
    redirect_contacts = reverse("info-type", args=['contacts'])
    redirect_sign_up = reverse('sign_up')
    redirect_log_in = reverse('log_in')

    return render(request, 'welcome.html', {"redirect_about" : redirect_about, "redirect_contacts" : redirect_contacts,
                                            "redirect_sign_up" : redirect_sign_up, "redirect_log_in" : redirect_log_in})


def welcome_info_types(request, info_type: str):
    if info_type == 'about':
        return HttpResponse('Ещё в разработке\nТут будет инфа о нас')
    elif info_type == 'contacts':
        return HttpResponse('Ещё в разработке\nТут будут наши контакты')


def sign_up_page(request):
    userform = Sign_up_Form()
    return render(request, "index.html", {"form": userform, "semi_title": "Регистрация аккаунта"})


def log_in_page(request):
    userform = Log_in_Form()
    return render(request, "index.html", {"form": userform, "semi_title": "Вход в аккаунт"})


def sign_up_form(request):
    surname = request.POST.get('Surname')
    name = request.POST.get('Name')
    patronymic = request.POST.get('Patronymic')
    grade_c = request.POST.get('Grade_c')
    grade_b = request.POST.get('Grade_b')
    email = request.POST.get('Email')
    password = request.POST.get('Password')
    password2 = request.POST.get('Pssword2')
    if password == password2:
        return HttpResponse(f'Фамилия: {surname}, '
                            f'Имя: {name}, '
                            f'Отчество: {patronymic}, '
                            f'Класс: {grade_c}{grade_b}, '
                            f'Пароль: {password}, '
                            f'Пароль 2 раз: {password2}')
    else:
        error_text = 'Пароли в двух полях не совпадают, проверьте и напишите еще раз.'
        redirect_sign_up = reverse("sign_up")
        return render(request, "welcome_error.html", {"error_text" : error_text, "href" : redirect_sign_up})
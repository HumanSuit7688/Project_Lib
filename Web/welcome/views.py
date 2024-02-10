from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


def welcome(request):
    redirect_path_about = reverse("info-type", args=['about'])
    redirect_path_contacts = reverse("info-type", args=['contacts'])
    redirect_path_sign_up = reverse('sign_up')
    redirect_path_log_in = reverse('log_in')

    page = f"""
    <title>Lyceum Library</title>
    <h1><p style="text-align: center;">Сайт библиотеки Лицея № 1</p></h1>
    <div style="text-align: center; class = "buttons">
            <h3><blockquote><a href='{redirect_path_about}'>О нас</a></blockquote></h3>
            <h3><a href='{redirect_path_contacts}'>Контакты</a></h3>
    </div>
    <h3><p style="text-align: center;">Чтобы пользоваться нашим сервисом, вам нужно зарегистрироваться и пройти верификацию у завуча Лицея</p></h3>
    <div style="text-align: center; class = "buttons">
            <h3><blockquote><a href='{redirect_path_sign_up}'>Регистрация</a></blockquote></h3>
            <h3>или</h3>
            <h3><a href='{redirect_path_log_in}'>Вход</a></h3>
    </div>
    """

    return HttpResponse(page)


def welcome_info_types(request, info_type: str):
    if info_type == 'about':
        return HttpResponse('Ещё в разработке\nТут будет инфа о нас')
    elif info_type == 'contacts':
        return HttpResponse('Ещё в разработке\nТут будут наши контакты')


def sign_up(request):
    return HttpResponse('В разработке, тут будет регистрация')


def log_in(request):
    return HttpResponse('В разработке, тут будет вход в аккаунт')



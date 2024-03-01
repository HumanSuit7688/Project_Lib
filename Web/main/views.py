from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.db import models
from .models import Book
from django.shortcuts import render


def main(request):
    books_list = dlc_ret_books()
    books = ''
    for i in books_list:
        book_str = dlc_ret_book_str(i)
        book_id = i.get('id')
        redirect_book = reverse("book_info", args=[book_id])
        book_li = f'<li>{book_str} ---> <a href={redirect_book}>Подробнее<a></li>\n'
        books += book_li
    body_books = f'<ol> {books} </ol>'

    return render(request, 'main.html', {"body_books" : body_books})


def book_info(request, book_id : int):
    id = book_id

    book = Book.objects.get(id=id)
    author = book.author
    name = book.name
    public_office = book.public_office
    born_year = book.born_year
    pages = book.pages

    return render(request, 'book_info.html', {"author": author, "name": name, "public_office": public_office, "public_year": born_year, "pages": pages})



def dlc_ret_books():
    books_db = Book.objects.all()
    books_list = []

    for i in books_db:
        books_dict = {'id' : i.id, 'author' : i.author, 'name' : i.name, 'public_office' : i.public_office, 'born_year' : i.born_year, 'pages' : i.pages}
        books_list.append(books_dict)

    return books_list


def dlc_ret_book_str(book):
    book_str = f'{book.get("author")} --- {book.get("name")}'
    return book_str

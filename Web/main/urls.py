from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name = 'main'),
    path('book_info/<int:book_id>', views.book_info, name='book_info'),
]



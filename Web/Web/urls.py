from django.urls import path
from welcome import views

urlpatterns = [
    path('', views.test, name='home'),
]

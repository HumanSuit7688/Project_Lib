from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome),
    path('sign_up/process/', views.sign_up_form, name='sign_up-process'),
    path('sign_up', views.sign_up_page, name='sign_up'),
    path('log_in', views.log_in_page, name ='log_in'),
    path('<str:info_type>', views.welcome_info_types, name='info-type'),

]

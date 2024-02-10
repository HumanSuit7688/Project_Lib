from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome),
    path('sign_up', views.sign_up, name='sign_up'),
    path('log_in', views.log_in, name ='log_in'),
    path('<str:info_type>', views.welcome_info_types, name='info-type'),

]

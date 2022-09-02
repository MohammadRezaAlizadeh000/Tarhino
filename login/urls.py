from django.urls import path
from . import views

urlpatterns = [
    path('login_register', views.login_register_page, name='login_register_page'),
]

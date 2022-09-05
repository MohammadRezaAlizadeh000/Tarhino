from django.urls import path
from .views import *

urlpatterns = [
    path('', start_home_page, name='start_home_page')
]
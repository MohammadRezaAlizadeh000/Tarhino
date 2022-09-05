from django.db import models


class LoginModel(models.Model):
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)


class RegisterModel(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

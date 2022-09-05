from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from .models import RegisterModel, LoginModel
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


def registration_page(request):
    if request.method == 'POST':
        register_form = RegistrationForm(request.POST)
        if register_form.is_valid():
            user = register_form.save()
            login(request, user)
            return redirect('start_home_page')
    else:
        register_form = RegistrationForm()

    return render(request, 'login/registration.html', {'register_form': register_form})


def login_page(request):
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@2')
    if request.method == 'POST':
        email = request.POST['user_name']
        password = request.POST['password']
        print(email)
        user = authenticate(request, email=email, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('start_home_page')
        else:
            login_form = LoginForm()
    else:
        login_form = LoginForm()

    return render(request, 'login/login.html', {'login_form': login_form})


@login_required
def logout_user(request):
    logout(request)
    return redirect('login_page')

from django.shortcuts import render


def login_register_page(request):
    if request.method == 'POST':
        username = request.POST['user_name']
        email = request.POST['email']
        password = request.POST['password']
        print(username)
        print(email)
        print(password)
    return render(request, 'login/login_register.html')

from django.shortcuts import render


def start_home_page(request):
    return render(request, 'publicPages/index.html')

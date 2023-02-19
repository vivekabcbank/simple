from django.shortcuts import render


def home(request):
    return render(request, 'core/index.html')

def login(request):
    return render(request, 'authentication/login.html')

def register(request):
    return render(request, 'authentication/register.html')

def forgotPassword(request):
    return render(request, 'authentication/forgot-password.html')

def error404(request):
    return render(request, 'authentication/error-404.html')

def blankPage(request):
    return render(request, 'blank-page.html')




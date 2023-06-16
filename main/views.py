from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegistrationForm
from django.shortcuts import render, redirect
from django.contrib.auth import logout
import os


def indx(request):
    data = {
        'title': 'Pagina principala',
        'values': ['some', 'Hello', '1234'],
        'obj': {
            'car': 'Toyota',
            'age': 18,
            'bobby': 'Fotball'
        }
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')


def footer_view(request):
    return render(request, 'main/footer.html')

def contact(request):
    return render(request, 'main/contact.html')


def download_cv(request):
    # Calea către fișierul PDF al CV-ului
    cv_file_path = os.path.join(settings.MEDIA_ROOT, 'cv.pdf')

    # Deschide fișierul PDF în mod binar
    with open(cv_file_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=cv.pdf'

    return response


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Inlocuieste 'nume_pagina' cu pagina dorita dupa autentificare
                return redirect('main/index.html')
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form})


def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Inlocuieste 'nume_pagina' cu pagina dorita dupa inregistrare
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'main/register.html', {'form': form})


def logout_view(request):
    logout(request)
    # Redirecționează către pagina principală după delogare
    return redirect('home')

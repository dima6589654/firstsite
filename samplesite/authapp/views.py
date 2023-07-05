from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from authapp.forms import UserLoginForm


def login(request):
    login_form = UserLoginForm(data=request.POST)

    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user and user.is_active:
            auth.login(request, user)

            # Запись данных запроса в файл
            with open('request_logs.txt', 'a', encoding='utf-8') as file:
                file.write(f"Запрос: username={username},password={password}, IP={request.META.get('REMOTE_ADDR')}\n")

            return HttpResponseRedirect(reverse('index'))

    return render(request, 'authapp/login.html', {'login_form': login_form})


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))

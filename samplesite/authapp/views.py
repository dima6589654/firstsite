from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

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


from django import forms


class UserDetailForm(forms.Form):
    username = forms.CharField(max_length=100)


class AllUsersView(View):
    def get(self, request):
        users = User.objects.all()
        context = {
            'users': users
        }
        return render(request, 'authapp/all_users.html', context)


class UserDetailView(View):
    def get(self, request):
        form = UserDetailForm()
        context = {
            'form': form,
        }
        return render(request, 'authapp/user_detail_form.html', context)

    def post(self, request):
        form = UserDetailForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            try:
                user = User.objects.get(username=username)
                context = {
                    'user': user,
                }
                return render(request, 'authapp/user_detail.html', context)
            except User.DoesNotExist:
                error_message = f"Пользователя с именем '{username}' не существует."
                return render(request, 'authapp/user_detail_form.html', {'form': form, 'error_message': error_message})
        else:
            return render(request, 'authapp/user_detail_form.html', {'form': form})

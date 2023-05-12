from django.shortcuts import render


def about(request):
    return render(request, 'about.html')


def home(request):
    context = {"work": "Главная страница сайта"}

    return render(request, 'home.html',context)


def contacts(request):
    return render(request, 'contacts.html')

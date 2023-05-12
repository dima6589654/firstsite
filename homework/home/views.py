from django.shortcuts import render


def about(request):
    return render(request, 'about.html')


def home(request):
    context = {"work": ""}

    return render(request, 'home.html',context)


def contacts(request):
    return render(request, 'contacts.html')

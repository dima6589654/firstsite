from django.shortcuts import render
from django.views import View
from .forms import PersonForm, ChildForm, IceCreamForm, IceCreamKioskForm


class PersonFormView(View):
    @staticmethod
    def get(request):
        form = PersonForm()
        return render(request, 'person_form.html', {'form': form})

    @staticmethod
    def post(request):
        form = PersonForm(request.POST)
        if form.is_valid():
            # Обработка валидной формы
            form.save()
            return render(request, 'person_success.html')
        return render(request, 'person_form.html', {'form': form})


class ChildFormView(View):
    @staticmethod
    def get(request):
        form = ChildForm()
        return render(request, 'child_form.html', {'form': form})

    @staticmethod
    def post(request):
        form = ChildForm(request.POST)
        if form.is_valid():
            # Обработка валидной формы
            form.save()
            return render(request, 'child_success.html')
        return render(request, 'child_form.html', {'form': form})


class IceCreamFormView(View):
    @staticmethod
    def get(request):
        form = IceCreamForm()
        return render(request, 'icecream_form.html', {'form': form})

    @staticmethod
    def post(request):
        form = IceCreamForm(request.POST)
        if form.is_valid():
            # Обработка валидной формы
            form.save()
            return render(request, 'icecream_success.html')
        return render(request, 'icecream_form.html', {'form': form})


class IceCreamKioskFormView(View):
    @staticmethod
    def get(request):
        form = IceCreamKioskForm()
        return render(request, 'kiosk_form.html', {'form': form})

    @staticmethod
    def post(request):
        form = IceCreamKioskForm(request.POST)
        if form.is_valid():
            # Обработка валидной формы
            form.save()
            return render(request, 'kiosk_success.html')
        return render(request, 'kiosk_form.html', {'form': form})

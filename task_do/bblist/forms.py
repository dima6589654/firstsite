# -*- coding: utf-8 -*-
from django import forms
from django.forms import DateTimeInput
from bblist.models import Task
from bblist.models import IceCream
from captcha.fields import CaptchaField


class TaskForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Task
        fields = ('title', 'description','priority' , 'due_date')
        widgets = {
            'due_date': DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class IceCreamForm(forms.ModelForm):
    class Meta:
        model = IceCream
        fields = ('flavor', 'topping', 'price')


class SearchForm(forms.Form):
    keyword = forms.CharField(max_length=20, label="Поиск")

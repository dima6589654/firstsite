# -*- coding: utf-8 -*-
from django import forms
from django.core.validators import FileExtensionValidator

from bblist.models import IceCream
from .models import Task


class TaskForm(forms.ModelForm):
    # captcha = CaptchaField()

    class Meta:
        model = Task
        fields = ('title', 'description', 'attachment', 'priority', 'due_date')
        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    attachment = forms.FileField(
        validators=[
            FileExtensionValidator(
                allowed_extensions=['pdf', 'xlsx', 'gif', 'jpg', 'png', 'doc', 'txt', 'zip'],
                message='Поддерживаются только файлы PDF, XLSX, GIF, JPG, PNG, DOC, TXT и ZIP.',

            )
        ]
    )


class IceCreamForm(forms.ModelForm):
    class Meta:
        model = IceCream
        fields = ('flavor', 'topping', 'price')


class SearchForm(forms.Form):
    keyword = forms.CharField(max_length=20, label="Поиск")

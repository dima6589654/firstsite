from django import forms
from django.forms import DateTimeInput
from bblist.models import Task
from bblist.models import IceCream


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title','priority', 'due_date')
        widgets = {
            'due_date': DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class IceCreamForm(forms.ModelForm):
    class Meta:
        model = IceCream
        fields = ('flavor', 'topping', 'price')

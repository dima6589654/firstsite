from django import forms
from django.forms import DateTimeInput
from bblist.models import Task
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'priority', 'due_date')
        widgets = {
            'due_date': DateTimeInput(attrs={'type': 'datetime-local'}),
        }
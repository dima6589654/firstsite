# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import TodoList, Category


class TaskForm(forms.ModelForm):
    """
    Форма для создания и редактирования задач.

    Attributes:
        title (str): Заголовок задачи.
        content (str): Описание задачи.
        due_date (date): Срок выполнения задачи.
        category (Category): Категория задачи.

    Meta:
        model (TodoList): Модель задачи.
        fields (list): Список полей, которые будут использоваться в форме.
        widgets (dict): Настройки виджетов для полей формы.

    """
    class Meta:
        model = TodoList
        fields = ['title', 'content', 'due_date', 'category']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }


class CategoryForm(forms.ModelForm):
    """
    Форма для создания и редактирования категорий.

    Attributes:
        name (str): Название категории.

    Meta:
        model (Category): Модель категории.
        fields (list): Список полей, которые будут использоваться в форме.

    """
    class Meta:
        model = Category
        fields = ['name']

    def __init__(self, *args, **kwargs):
        """
        Инициализация формы категории.

        Args:
            *args: Позиционные аргументы.
            **kwargs: Именованные аргументы.

        """
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'Название категории'
        self.fields['name'].widget.attrs.update({'class': 'form-control'})


class CustomUserCreationForm(UserCreationForm):
    """
    Форма для создания пользователей с дополнительными настройками.

    Meta:
        model (User): Модель пользователя.
        fields (tuple): Список полей, которые будут использоваться в форме.

    """
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        """
        Инициализация формы создания пользователя.

        Args:
            *args: Позиционные аргументы.
            **kwargs: Именованные аргументы.

        """
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = None
        self.fields['password1'].help_text = 'Ваш пароль должен содержать как минимум 8 символов.'
        self.fields['password2'].help_text = 'Введите пароль ещё раз для подтверждения.'

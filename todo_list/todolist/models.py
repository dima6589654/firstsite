# -*- coding: utf-8 -*-

from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """
    Модель для представления категорий задач.

    Attributes:
        name (str): Название категории.

    Methods:
        __str__: Возвращает строковое представление объекта категории.
    """
    name = models.CharField(max_length=100, verbose_name="Название категории")

    def __str__(self):
        """
        Возвращает строковое представление объекта категории.
        """
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class TodoList(models.Model):
    """
    Модель для представления задач в списке дел.

    Attributes:
        title (str): Заголовок задачи.
        content (str): Описание задачи.
        created (datetime): Дата и время создания задачи.
        due_date (datetime): Срок выполнения задачи.
        category (Category): Связь с категорией задачи.
        user (User): Связь с пользователем (автором задачи).

    Methods:
        __str__: Возвращает строковое представление объекта задачи.
    """
    title = models.CharField(max_length=250, verbose_name="Заголовок")
    content = models.TextField(blank=True, verbose_name="Описание")
    created = models.DateField(default=timezone.now, verbose_name="Дата создания")
    due_date = models.DateField(default=timezone.now, verbose_name="Срок выполнения")
    category = models.ForeignKey(Category, default=None, on_delete=models.PROTECT, verbose_name="Категория", null=True,
                                 blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")

    def __str__(self):
        """
        Возвращает строковое представление объекта задачи.
        """
        return self.title

    class Meta:
        ordering = ["-created"]
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

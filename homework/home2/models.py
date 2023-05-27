from django.db import models


class Questionnaire(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    age = models.PositiveIntegerField(verbose_name="Возраст")
    email = models.EmailField()

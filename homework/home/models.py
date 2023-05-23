from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=50,verbose_name="Имя")
    age = models.PositiveIntegerField(verbose_name="Возраст")


class Child(models.Model):
    name = models.CharField(max_length=50,verbose_name="Имя")
    age = models.PositiveIntegerField(verbose_name="Возраст")
    parent = models.ForeignKey('Person', on_delete=models.CASCADE,verbose_name="Родитель")


class IceCream(models.Model):
    flavor = models.CharField(max_length=50,verbose_name="Вкус")
    price = models.DecimalField(max_digits=5, decimal_places=2,verbose_name="Цена")


class IceCreamKiosk(models.Model):
    name = models.CharField(max_length=50,verbose_name="Название")
    location = models.CharField(max_length=100, verbose_name="Местоположение")
    ice_creams = models.ManyToManyField('IceCream',verbose_name="Мороженое")

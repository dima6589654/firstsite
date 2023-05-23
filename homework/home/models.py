from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()


class Child(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    parent = models.ForeignKey('Person', on_delete=models.CASCADE)


class IceCream(models.Model):
    flavor = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)


class IceCreamKiosk(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    ice_creams = models.ManyToManyField('IceCream')

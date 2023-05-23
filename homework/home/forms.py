from django import forms
from .models import Person, Child, IceCream, IceCreamKiosk


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'age']


class ChildForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['name', 'age', 'parent']


class IceCreamForm(forms.ModelForm):
    class Meta:
        model = IceCream
        fields = ['flavor', 'price']


class IceCreamKioskForm(forms.ModelForm):
    class Meta:
        model = IceCreamKiosk
        fields = ['name', 'location', 'ice_creams']

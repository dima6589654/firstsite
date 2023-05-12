from django.forms import ModelForm
from home.models import Bb


class Home(ModelForm):
    class Meta:
        model = Bb
        fields = ('title', 'content', 'price', 'rubric')

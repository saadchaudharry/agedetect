from django import forms
from .models import Imagemodels

class Imagemodelform(forms.ModelForm):
    class Meta:
        model =Imagemodels
        fields=['name','image']
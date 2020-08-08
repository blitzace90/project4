from django import forms
from .models import Furniture
from cloudinary.forms import CloudinaryJsFileField


class FurnitureForm(forms.ModelForm):
    class Meta:
        model = Furniture
        fields = ('name', 'model', 'desc', 'quantity', 'category', 'color', 'picture')
    picture = CloudinaryJsFileField()

class SearchForm(forms.Form):
    name = forms.CharField(max_length=100, required=False)


from django import forms
from .models import Furniture
from cloudinary.forms import CloudinaryJsFileField
from django.views.generic import ListView


class SearchForm(forms.Form):
    name = forms.CharField(max_length=100, required=False, label="", widget=forms.TextInput(
        attrs={'placeholder': 'Search entire store'}))


class FurnitureForm(forms.ModelForm):
    class Meta:
        model = Furniture
        fields = ('name', 'model', 'desc', 'quantity', 'category', 'tags', 'color', 'materials', 'height', 'breath', 'length', 'weight', 'cost', 'picture')

    picture = CloudinaryJsFileField()

class FurnitureList(ListView):
    paginate_by = 2
    model = Furniture

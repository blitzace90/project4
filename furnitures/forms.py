from django import forms
from .models import Furniture
from cloudinary.forms import CloudinaryJsFileField
from crispy_forms.helper import FormHelper


class SearchForm(forms.Form):
    name = forms.CharField(max_length=100, required=False, label="", widget=forms.TextInput(
        attrs={'placeholder': 'Search entire store'}))

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper(self)
    #     self.helper.form_show_labels = False

from django import forms
from .models import Comment, Feedback
from cloudinary.forms import CloudinaryJsFileField


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'phone', 'email', 'comments']


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['order', 'description', 'image']

    image = CloudinaryJsFileField()

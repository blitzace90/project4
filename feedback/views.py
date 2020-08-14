from django.shortcuts import render, get_object_or_404
from django.contrib import messages

# Create your views here.
def contact(request):
    return render(request, 'feedback/contact.template.html')

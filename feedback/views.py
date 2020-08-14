from django.shortcuts import render
from django.contrib import messages
from .forms import CommentForm

# Create your views here.
def contact(request):
    if request.method == 'POST':
        print(request.POST)

        form = CommentForm(request.POST)
        form.save()
        return render(request, 'feedback/contact.template.html', {
            'form': form
        })

    else:
        form = CommentForm()
        return render(request, 'feedback/contact.template.html', {
            'form': form
        })

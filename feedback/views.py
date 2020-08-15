from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CommentForm, FeedbackForm

# Create your views here.
def contact(request):
    if request.method == 'POST':
        print(request.POST)

        form = CommentForm(request.POST)
        form.save()
        messages.success(request, "Thanks for your feedback!")
        return redirect('contact')

    else:
        form = CommentForm()
        return render(request, 'feedback/contact.template.html', {
            'form': form
        })

def feedback(request):
    if request.method == 'POST':
        print(request.POST)

        form = FeedbackForm(request.POST)
        feedback = form.save()
        feedback.owner = request.user
        feedback.save()
        messages.success(request, "Thanks for your feedback! We will look into this matter.")
        return redirect('feedback')

    else:
        form = FeedbackForm()
        return render(request, 'feedback/feedback.template.html', {
            'form': form
        })

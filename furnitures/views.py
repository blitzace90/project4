from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Furniture
from .forms import FurnitureForm, SearchForm

# Create your views here.


def index(request):
    furnitures = Furniture.objects.all()

    if request.GET:
        queries = ~Q(pk__in=[])

        if 'name' in request.GET and request.GET['name']:
            name = request.GET['name']
            queries = queries & Q(name__icontains=name)

        furnitures = furnitures.filter(queries)

    search_form = SearchForm(request.GET)

    return render(request, 'furnitures/index.template.html', {
        'furnitures': furnitures,
        'search_form': search_form
    })


@login_required 
def create_furniture(request):
    if request.method == 'POST':
        print(request.POST)

        form = FurnitureForm(request.POST)
        form.save()
        return HttpResponse("Form received")

    else:
        form = FurnitureForm()
        return render(request, 'furnitures/create_furniture.template.html', {
            'form': form
        })


def show_furnitures(request):
    furnitures = Furniture.objects.all()
    return render(request, 'furnitures/list_furnitures.template.html', {
        'furnitures': furnitures
    })



from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Furniture
from .forms import SearchForm

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


def show_furnitures(request):
    furnitures = Furniture.objects.all()
    return render(request, 'furnitures/list_furnitures.template.html', {
        'furnitures': furnitures
    })


def furniture_details(request, furniture_id):
    furniture = get_object_or_404(Furniture, pk=furniture_id)
    return render(request, 'furnitures/furniture_details.template.html', {
        "furniture": furniture
    })

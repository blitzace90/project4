from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Furniture, Category
from .forms import SearchForm, FurnitureForm
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, 'furnitures/index.template.html')


def about(request):
    return render(request, 'furnitures/aboutus.template.html')


def create_furnitures(request):
    if request.method == 'POST':
        form = FurnitureForm(request.POST)
        form.save()
        messages.success(request, "New furniture has been created")
        return redirect(reverse(show_furnitures))

    else:
        form = FurnitureForm()
        return render(request, 'furnitures/create_furniture.template.html', {
            'form': form
        })


def show_furnitures(request):
    furnitures = Furniture.objects.all()

    if request.GET:
        queries = ~Q(pk__in=[])

        if 'name' in request.GET and request.GET['name']:
            name = request.GET['name']
            queries = queries & Q(name__icontains=name)

        furnitures = furnitures.filter(queries)

    search_form = SearchForm(request.GET)

    return render(request, 'furnitures/list_furnitures.template.html', {
        'furnitures': furnitures,
        'search_form': search_form
    })


def filter_furnitures(request, category_filter):

    furnitures = Furniture.objects.all()
    furnitures = furnitures.filter(category__category=category_filter)

    return render(request, "furnitures/list_furnitures.template.html", {
        'furnitures': furnitures,
    })


def furniture_details(request, furniture_id):
    furniture = get_object_or_404(Furniture, pk=furniture_id)
    return render(request, 'furnitures/furniture_details.template.html', {
        "furniture": furniture
    })


def edit_furnitures(request, furniture_id):
    furniture = get_object_or_404(Furniture, pk=furniture_id)
    if request.method == "POST":
        form = FurnitureForm(request.POST, instance=furniture)
        if form.is_valid():
            form.save()
            messages.success(request, f"furniture updated")
            return redirect('furniture_details', furniture_id=furniture.id)
        else:
            return render(request, 'furnitures/edit_furniture.template.html', {
            'form': form,
            })

    else:
        form = FurnitureForm(instance=furniture)
        return render(request, 'furnitures/edit_furniture.template.html', {
            'form': form,
            'furniture': furniture
        })


def delete_furnitures(request, furniture_id):
    furniture = get_object_or_404(Furniture, pk=furniture_id)
    furnitures = Furniture.objects.all()
    if request.method == 'POST':
        furniture.delete()
        messages.success(request, "Furniture has been deleted")
        return render(request, 'furnitures/list_furnitures.template.html', {
            'furnitures': furnitures
        })

    else:
        return render(request, 'furnitures/confirm_delete.template.html', {
            'furniture': furniture
        })

from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from django.contrib import messages

from furnitures.models import Furniture

# Create your views here.
def add_to_cart(request, furniture_id):
    cart = request.session.get('shopping_cart', {})
    if furniture_id not in cart:
        furniture = get_object_or_404(Furniture, pk=furniture_id)
        # book is found, let's add it to the cart
        cart[furniture_id] = {
            'id': furniture_id,
            'name': furniture.name,
            'cost': 99,
            'qty': 1
        }
        # save the cart back to sessions
        request.session['shopping_cart'] = cart
        messages.success(request, "Furniture has been added to your cart!")
        return HttpResponse('book added')
    else:
        cart[furniture_id]['qty'] += 1
        request.session['shopping_cart'] = cart
        return HttpResponse('book added')

def view_cart(request):
    cart = request.session['shopping_cart']
    return render(request, 'view_cart.template.html', {
        'cart': cart
    })
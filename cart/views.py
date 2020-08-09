from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from django.contrib import messages

from furnitures.models import Furniture

# Create your views here.
def add_to_cart(request, furniture_id):
    cart = request.session.get('shopping_cart', {})
    furniture = get_object_or_404(Furniture, pk=furniture_id)
    quantity = request.POST.get('quantity')
    if furniture_id not in cart:
        # book is found, let's add it to the cart
        cart[furniture_id] = {
            'id': furniture_id,
            'name': furniture.name,
            'cost': float(furniture.cost),
            'qty': int(request.POST.get('quantity')),
            'total_cost': float(furniture.cost)
        }

        messages.success(request, f"Added {quantity} '{furniture.name}' to the shopping cart")

    else:
        cart[furniture_id]['qty'] += int(request.POST.get('quantity'))
        messages.success(request, f"Added {quantity} '{furniture.name}' to the shopping cart")

    request.session['shopping_cart'] = cart
    return redirect('furniture_details', furniture.id)


def view_cart(request):
    cart = request.session['shopping_cart']

    total = 0
    for k, v in cart.items():
        total += float(v['cost']) * int(v['qty'])

    return render(request, 'cart/view_cart.template.html', {
        'cart': cart,
        'total': total
    })


def remove_from_cart(request, furniture_id):
    cart = request.session['shopping_cart']
    if furniture_id in cart:
        del cart[furniture_id]
        request.session['shopping_cart'] = cart
        messages.success(request, 'the item has been removed')

    return redirect(reverse('view_cart'))


def update_quantity(request, furniture_id):
    cart = request.session['shopping_cart']
    if furniture_id in cart:
        cart[furniture_id]['qty'] = request.POST['qty']
        cart[furniture_id]['total_cost'] = int(request.POST['qty']) * float(cart[furniture_id]['cost'])

        request.session['shopping_cart'] = cart
        messages.success(request, f"Quantity for {cart[furniture_id]['name']} has been updated")

        return redirect(reverse('view_cart'))

    else:

        return redirect(reverse('view_cart'))

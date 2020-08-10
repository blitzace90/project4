from django.shortcuts import render, get_object_or_404, HttpResponse, reverse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.sites.models import Site
from furnitures.models import Furniture

import stripe

# Create your views here.


@login_required
def checkout(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY

    cart = request.session.get('shopping_cart', {})

    line_items = []

    for furniture_id, furniture in cart.items():
        furniture_model = get_object_or_404(Furniture, pk=furniture_id)

        item = {
            "name": furniture_model.name,
            "amount": int(furniture_model.cost * 100),
            "quantity": furniture['qty'],
            "currency": "sgd"
        }

        line_items.append(item)

    current_site = Site.objects.get_current()

    domain = current_site.domain

    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=line_items,
        success_url=domain + reverse("checkout_success"),
        cancel_url=domain + reverse("checkout_cancelled")
    )

    return render(request, "checkout/checkout.template.html", {
        "session_id": session.id,
        "public_key": settings.STRIPE_PUBLISHABLE_KEY
    })


def checkout_success(request):
    return HttpResponse("checkout successs")


def checkout_cancelled(request):
    return HttpResponse("checkcout cancelled")


@csrf_exempt
def payment_completed(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    endpoint_secret = "whsec_4LJT2xOTigTblomiW3dJLITAbvOxPJ6W"

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret)
    except ValueError:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

        # Fulfill the purchase...
        handle_payment(session)

    return HttpResponse(status=200)

def handle_payment(session):
    print(session)
    pass

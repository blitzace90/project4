from django.urls import path

import feedback.views

urlpatterns = [
    path('', feedback.views.contact, name='contact'),
]
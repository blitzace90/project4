from django.urls import path

import feedback.views

urlpatterns = [
    path('comment/', feedback.views.contact, name='contact'),
    path('review/', feedback.views.feedback, name='feedback')
]
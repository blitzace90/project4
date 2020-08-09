from django.urls import path

import furnitures.views

urlpatterns = [
    path('create/', furnitures.views.create_furniture),
    path('all/', furnitures.views.show_furnitures, name='show_all_furnitures'),
    path('<furniture_id>/', furnitures.views.furniture_details, name='furniture_details'),
]
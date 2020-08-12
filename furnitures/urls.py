from django.urls import path

import furnitures.views

urlpatterns = [
    path('all/', furnitures.views.show_furnitures, name='show_all_furnitures'),
    path('<furniture_id>/', furnitures.views.furniture_details, name='furniture_details'),
    path('filter/<category>', furnitures.views.filter_furnitures, name="filter"),
]
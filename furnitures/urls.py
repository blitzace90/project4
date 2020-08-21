from django.urls import path

import furnitures.views

urlpatterns = [
    path('create', furnitures.views.create_furnitures, name='create_furnitures'),
    path('all/', furnitures.views.show_furnitures, name='show_all_furnitures'),
    path('about', furnitures.views.about, name='aboutus'),
    path('<furniture_id>/', furnitures.views.furniture_details, name='furniture_details'),
    path('filter/<category_filter>', furnitures.views.filter_furnitures, name="filter"),
    path('<furniture_id>/edit', furnitures.views.edit_furnitures, name='edit_furnitures'),
    path('<furniture_id>/delete', furnitures.views.delete_furnitures, name='delete_furnitures')
]
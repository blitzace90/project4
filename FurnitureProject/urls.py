"""FurnitureProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import furnitures.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('furnitures/create/', furnitures.views.create_furniture),
    path('accounts/', include('allauth.urls')),
    path('home/', furnitures.views.index, name='home_page'),
    path('furnitures/all/', furnitures.views.show_furnitures, name='show_all_furnitures'),
    path('furnitures/<furniture_id>', furnitures.views.furniture_details, name='furniture_details'),
    path('cart/', include('cart.urls'))
]

"""django_cookie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from rest_framework.routers import DefaultRouter

from main_app.views.fetch_data import FetchPizzasViewSet
from main_app.views.statistics import StatisticsViewSet

router = DefaultRouter()

urlpatterns = [
    path(
        "fetch_data/",
        FetchPizzasViewSet.as_view({"get": "fetch_data"}),
        name="fetch_data",
    ),
    path(
        "get_most_popular_pizza/",
        StatisticsViewSet.as_view({"get": "get_most_popular_pizza"}),
        name="get_most_popular_pizza",
    ),
    path(
        "get_most_popular_pizza_day/",
        StatisticsViewSet.as_view({"get": "get_most_popular_pizza_day"}),
        name="get_most_popular_pizza_day",
    ),
    path(
        "get_most_popular_pizza_ingredients/",
        StatisticsViewSet.as_view({"get": "get_most_popular_pizza_ingredients"}),
        name="get_most_popular_pizza_ingredients",
    ),
    path(
        "get_most_popular_pizza_ingredients/",
        StatisticsViewSet.as_view({"get": "get_most_popular_pizza_ingredients"}),
        name="get_most_popular_pizza_ingredients",
    ),
] + router.urls

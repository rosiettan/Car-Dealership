from django.contrib import admin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import path

from market.views_auth import login, logout
from views_weather import show_weather
from market.views import shows_cars, audi_purchase, payment


def hello_world(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello_world),
    path('weather', show_weather),
    path('audi', shows_cars),
    path('buy_car/<int:id_>', audi_purchase),
    path('payment/<int:id_>', payment),
    path('login', login),
    path('logout', logout),
]

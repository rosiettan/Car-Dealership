from django.contrib import admin
from django.http import HttpRequest, HttpResponse
from django.urls import path
import random


def show_weather(request: HttpRequest) -> HttpResponse:
    temprature = random.randint(-40, 40)
    feel = "OK"
    if temprature > 20:
        feel = "hot"
    if temprature < 0:
        feel = "cold"
    if temprature < -10:
        feel = "terribly cold"
    return HttpResponse(f"Today: {temprature} grad celsius, it is {feel}")
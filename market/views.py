from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from market.models import Car, Order, Payment


def show_cars(request: HttpRequest) -> HttpResponse:
    user = request.user
    if not user.is_authenticated:
        return HttpResponseRedirect("/login")


def audi_purchase(request: HttpRequest, id_: int) -> HttpResponse:
    car = Car.objects.filter(id=id_).first()

    if request.method == "POST":
        order = Order.objects.create(
            car=car,
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
        )
        return HttpResponseRedirect("/audi")

    return render(request, "purchase_form.html", {"car": car})


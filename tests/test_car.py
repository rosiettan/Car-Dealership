from django import TestCase
from django.contrib.auth.models import User

from market.models import Car, Purchase, Order, Payment


class PurchaseTest(TestCase):
    def setUp(self):
        Car.objects.create(name="Audi A6")
        Car.objects.create(name="Audi A7")
        Car.objects.create(name="Audi A8")
        User.objects.create_user(username="bill", password="gates")
        response = self.client.get("/")
        self.client.post(response.url, {
            "username": "bill",
            "password": "gates",
        })

    def test_car_count(self):
        self.assertEqual(Car.objects.all().count(), 2)
        car = Car.objects.get(name="Audi A7")
        assert car.name == "Audi A7"

    def test_cars_left_function(self):
        car = Car.objects.get(name="Audi A6")
        # buy 3 cars
        Purchase.objects.create(car=car)
        Purchase.objects.create(car=car)
        Purchase.objects.create(car=car)
        # sell 1 car
        Order.objects.create(car=car)
        # we should have 2 cars left
        self.assertEqual(car.cars_left(), 2)
        car = Car.objects.get(name="Audi A7")
        self.assertEqual(car.cars_left(), 0)

    # ???
    def assertEqual(self, param, param1):
        pass

    def test_cars_orders_by_client(self):
        # buy_car/<int:id_>
        car = Car.objects.get(name="Audi A6")
        # buy 3 cars
        Purchase.objects.create(car=car)
        Purchase.objects.create(car=car)
        Purchase.objects.create(car=car)
        # sell 1 car
        url = f"buy_car/{car.id}"
        response = self.client.post(url, {
            "name": "Raziya",
            "email": "rosiettan@mail.ru",
            "phone": "77088236797",
        })

        self.assertEqual(response.status_code, 302)
        assert car.cars_left() == 2

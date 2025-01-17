from django import TestCase
from django.contrib.auth.models import User

from market.models import Car, Purchase, Order, Payment


class PurchaseTest(TestCase):
    def setUp(self):
        User.objects.create_user(username="bill", password="gates")

    def test_correct_login(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 302)
        response = self.client.post(response.url, {
            "username": "bill",
            "password": "gates",
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/")

    def test_incorrect_login(self):
        response = self.client.get("/")

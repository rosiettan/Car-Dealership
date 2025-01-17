from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    available = models.IntegerField(default=0)
    image = models.CharField(max_length=1000, blank=True, default="")
    price = models.IntegerField(default=0)

    def cars_left(self) -> int:
        ordered = Order.objects.filter(car=self).count()
        purchased = 0
        for purchase in Purchase.objects.filter(car=self):
            purchased += purchase.count
        return purchased - ordered

    def __str__(self):
        return f"{self.id}: {self.name}, available: {self.available}"


class Order(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=15)
    status = models.CharField(max_length=100, default="created")

    def __str__(self):
        return f"{self.id}: {self.name}, " \
               f"phone: {self.phone}, status: {self.status}"


class Purchase(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.car}, purchased on date {self.date}"

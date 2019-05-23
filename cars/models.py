from django.db import models

from django.contrib.auth.models import User
from accounts.models import Seller

from django.core import validators
from phonenumber_field.modelfields import PhoneNumberField
from .enums import MakeEnum, FuelEnum, ColorEnum, BodyTypeEnum

# Create your models here.


class Car(models.Model):
    owner = models.ForeignKey(Seller, on_delete=models.CASCADE)

    make = models.CharField(
        max_length=10, choices=[(m.name, m.value) for m in MakeEnum]
    )
    model = models.CharField(max_length=10)
    fuel = models.CharField(
        max_length=10, choices=[(f.name, f.value) for f in FuelEnum]
    )
    color = models.CharField(
        max_length=10, choices=[(c.name, c.value) for c in ColorEnum]
    )
    car_type = models.CharField(
        max_length=10, choices=[(b.name, b.value) for b in BodyTypeEnum]
    )
    picture = models.URLField()

    def __str__(self):
        return f"{self.owner} | car -  {self.make} {self.model} {self.car_type} {self.fuel} {self.color}"

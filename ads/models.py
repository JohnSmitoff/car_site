from django.db import models
from accounts.models import Seller
from cars.models import Car
from django.contrib.auth.models import User

from .enums import AdStatusEnum


# Create your models here.


class Advert(models.Model):
    ad_owner = models.ForeignKey(Seller, on_delete=models.CASCADE, default=Seller)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    ad_text = models.TextField(max_length=200)
    price = models.PositiveIntegerField(default=1)

    status = models.CharField(
        max_length=10,
        choices=[(st.name, st.value) for st in AdStatusEnum],
        default=AdStatusEnum.P,
    )
    creation_date = models.DateField()

    def __str__(self):
        return (
            f"created by {self.ad_owner} on {self.creation_date} status - {self.status}"
        )

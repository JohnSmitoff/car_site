from django.db import models

from django.contrib.auth.models import User

from django.core import validators
from phonenumber_field.modelfields import PhoneNumberField
from .enums import GenderEnum

# Create your models here.


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = PhoneNumberField()
    gender = models.CharField(
        max_length=10, choices=[(g.name, g.value) for g in GenderEnum]
    )

    def __str__(self):
        return f"{self.user} | number -  {self.phone_number} | sex - {self.gender}"


class Moderator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(
        max_length=10, choices=[(g.name, g.value) for g in GenderEnum]
    )

    def __str__(self):
        return f"{self.user}"

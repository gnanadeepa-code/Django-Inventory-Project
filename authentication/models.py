from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # You can add additional fields here if needed
    age = models.PositiveIntegerField(null=True, blank=True,default=0)

    role_choices = [
        (0, 'Employee'),
        (1, 'Manager'),
        (2, 'Admin'),
    ]

    role = models.IntegerField(choices=role_choices, default=2)
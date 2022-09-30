from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=50, blank=True, null=True, unique=True)
    email = models.EmailField(("email address"), unique=True)
    fullname = models.CharField(max_length=20,null=True)
    phonenumber = models.CharField(max_length=15,null=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username","first_name","last_name","phonenumber"]

    def __str__(self):
        return "{}".format(self.email)

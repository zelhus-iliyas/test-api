from django.db import models
from django.contrib.auth.models import AbstractUser


# class ClientUser(AbstractUser):
#     username = models.CharField(max_length=50, blank=True, null=True, unique=True)
#     email = models.EmailField(("email address"), unique=True)
#     full_name = models.CharField(max_length=50, blank=True, null=True, unique=True)
#     last_name = models.CharField(max_length=50, blank=True, null=True, unique=True)
#     phonenumber = models.CharField(max_length=15, null=True)

#     def __str__(self):
#         return "{}".format(self.email)


# from django.db import models
# from oauth2client.contrib.django_util.models import CredentialsField


# class Credentials(models.Model):
#     id = models.OneToOneField(ClientUser, primary_key=True)
#     credential = CredentialsField()

#     class Meta:
#         db_table = "credentials"

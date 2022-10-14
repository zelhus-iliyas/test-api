from django.db import models


from commFactsAdmin.models import User


class Client(models.Model):
    primary_contact_first_name = models.CharField(max_length=50)
    primary_contact_last_name = models.CharField(max_length=50)
    primary_contact_email = models.CharField(max_length=50, unique=True)
    primary_contact_phone_number = models.CharField(max_length=50, unique=True)
    primary_contact_phone_type = models.CharField(max_length=50)
    secondary_contact_first_name = models.CharField(max_length=50)
    secondary_contact_last_name = models.CharField(max_length=50)
    secondary_contact_email = models.CharField(max_length=50, unique=True)
    secondary_contact_phone_number = models.CharField(max_length=50, unique=True)
    secondary_contact_phone_type = models.CharField(max_length=50)
    street_address_line_1 = models.CharField(max_length=50)
    street_address_line_2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip = models.IntegerField()
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.primary_contact_email


class ClientCalenderTokenModel(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    access_token=models.CharField(max_length=300)
    refresh_token=models.CharField(max_length=300)
    token_uri=models.CharField(max_length=100)
    token_expiry=models.CharField(max_length=50)

    def __str__(self):
        return self.user.email
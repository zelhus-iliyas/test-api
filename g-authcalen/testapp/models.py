# from django.contrib import admin
from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.contrib.auth import get_user_model

# from oauth2client.contrib.django_util.models import CredentialsField
from django.contrib.auth.backends import ModelBackend
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class SignUpManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("insert user")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):

        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user


class User_Auth(models.Model):
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    USERNAME_FIELD = "email"
    objects = SignUpManager()

    def __str__(self):
        return self.email

    # @property
    # def is_authenticated(self):
    #     return True


# class EmailBackend(ModelBackend):
#     def authenticate(email=None):
#         UserModel = get_user_model()
#         # UserModel = User_Auth
#         user = UserModel.objects.get(email=email)
#         if user:
#             return user
#         else:
#             return None


# l = {"email": "shaik.iliyas@zelhus.com"}
# o = "afde65f0d6768afcf340d8e05567a49be6d66227"

# class StudentProfile(models.Model):
#     user = models.OneToOneField('User', related_name='student_profile',on_delete=True)
#     # additional fields for students

# class TeacherProfile(models.Model):
#     user = models.OneToOneField('User', related_name='teacher_profile',on_delete=True)
#     # additional fields for teachers


# class User(AbstractUser):
#     is_doctor = models.BooleanField(default=False)
#     is_patient = models.BooleanField(default=False)


# class Patient(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     user.is_patient = True
#     pid = models.AutoField(unique=True, primary_key=True)  # patient identification


# class Doctor(models.Model):
#     upin = models.AutoField(primary_key=True)  # unique physician identification number
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     user.is_doctor = True
#     expertise = models.CharField(max_length=20)
#     days_available = models.DateTimeField(null=True)


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         if instance.is_patient:
#             Patient.objects.create(user=instance)
#         elif instance.is_doctor:
#             Doctor.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     if instance.is_patient:
#         instance.patient.save()
#     elif instance.is_doctor:
#         instance.doctor.save()

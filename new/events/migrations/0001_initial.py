# Generated by Django 4.1 on 2022-09-22 07:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="EmailUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                ("first_name", models.CharField(max_length=30)),
                ("last_name", models.CharField(max_length=30)),
                ("username", models.CharField(max_length=30)),
                (
                    "email",
                    models.EmailField(
                        error_messages={
                            "unique": "That email address is already taken."
                        },
                        max_length=254,
                        unique=True,
                    ),
                ),
                ("is_staff", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "date_joined",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("last_updated", models.DateTimeField(auto_now=True)),
                (
                    "google_oauth2_client_id",
                    models.CharField(blank=True, default="", max_length=254),
                ),
                (
                    "google_oauth2_secrete",
                    models.CharField(blank=True, default="", max_length=254),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "ordering": ["-id"],
                "permissions": (("view_emailuser", "Can view email users"),),
                "default_permissions": ("add", "change", "delete"),
            },
        ),
        migrations.CreateModel(
            name="Oauth2Token",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        related_name="user_oauth2token",
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("access_token", models.CharField(default="", max_length=254)),
                ("refresh_token", models.CharField(default="", max_length=254)),
                ("token_expiry", models.CharField(default="", max_length=254)),
                ("code", models.CharField(blank=True, max_length=254)),
                ("text", models.TextField(blank=True, default="")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "UserOauth2Token",
                "verbose_name_plural": "UserOauth2Tokens",
                "ordering": ("user", "updated_at"),
                "managed": True,
                "unique_together": {("user",)},
            },
        ),
    ]

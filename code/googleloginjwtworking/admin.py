from django.contrib import admin
from .models import Client


class ClientAdmin(admin.ModelAdmin):
    list_display = [
        "primary_contact_first_name",
        "primary_contact_last_name",
        "primary_contact_email",
        "primary_contact_phone_number",
        "primary_contact_phone_type",
        "secondary_contact_first_name",
        "secondary_contact_last_name",
        "secondary_contact_email",
        "secondary_contact_phone_number",
        "secondary_contact_phone_type",
        "street_address_line_1",
        "street_address_line_2",
        "city",
        "state",
        "zip",
        "country",
    ]
    list_display_links = [
        "primary_contact_first_name",
        "primary_contact_last_name",
        "primary_contact_email",
    ]


admin.site.register(Client, ClientAdmin)

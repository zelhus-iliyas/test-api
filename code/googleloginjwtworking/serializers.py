from rest_framework import serializers

from .models import *


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


###if address in seperate table
# class AddressSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Address
#         fields = [
#             "street_address_line_1",
#             "street_address_line_2",
#             "city",
#             "state",
#             "zip",
#             "country",
#         ]


# class ClientSerializer(serializers.ModelSerializer):
#     address = AddressSerializer()

#     class Meta:
#         model = Client
#         fields = [
#             "primary_contact_first_name",
#             "primary_contact_last_name",
#             "primary_contact_email",
#             "primary_contact_phone_number",
#             "primary_contact_phone_type",
#             "secondary_contact_first_name",
#             "secondary_contact_last_name",
#             "secondary_contact_email",
#             "secondary_contact_phone_number",
#             "secondary_contact_phone_type",
#             "address",
#         ]
#     def create(self, validated_data):
#         address_data=validated_data.pop("address")
#         address_obj=Address.objects.create(**address_data)
#         address_id=address_obj.id
#         client = Client.objects.create(**validated_data,client_address_id=address_id)
#         return client

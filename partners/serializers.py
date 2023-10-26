from rest_framework import serializers
from .models import Customer, Consignee, Carrier, DeliveryAddress, Bank, Contact


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class ConsigneeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consignee
        fields = "__all__"


class CarrierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrier
        fields = "__all__"


class DeliveryAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryAddress
        fields = "__all__"
        extra_kwargs = {
            "address": {"required": False},
        }


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"

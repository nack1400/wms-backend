from rest_framework import serializers
from .models import Customer, Consignee, Carrier, CarrierAddress


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


class CarrierAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarrierAddress
        fields = "__all__"

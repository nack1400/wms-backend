from rest_framework import serializers
from .models import *


# Customer
class CustomerAttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerAttachment
        fields = (
            "id",
            "url",
        )


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class CustomerWithAttachmentsSerializer(CustomerSerializer):
    attachments = CustomerAttachmentSerializer(many=True)


# Consignee
class ConsigneeAttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsigneeAttachment
        fields = (
            "id",
            "url",
        )


class ConsigneeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consignee
        fields = "__all__"


class ConsigneeWithAttachmentsSerializer(ConsigneeSerializer):
    attachments = ConsigneeAttachmentSerializer(many=True)


# Carrier
class CarrierAttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarrierAttachment
        fields = (
            "id",
            "url",
        )


class CarrierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrier
        fields = "__all__"


class CarrierWithAttachmentsSerializer(CarrierSerializer):
    attachments = CarrierAttachmentSerializer(many=True)


# Delivery
class DeliveryAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryAddress
        fields = "__all__"


# Bank
class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = "__all__"


# Contact
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"

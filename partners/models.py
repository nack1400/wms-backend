from django.db import models
from common.models import CommonModel


class Customer(CommonModel):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    memo = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Consignee(CommonModel):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    memo = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Carrier(CommonModel):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    memo = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class CarrierAddress(CommonModel):
    carrier = models.ForeignKey(Carrier, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    memo = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.carrier.name} - {self.address}"


class Contact(CommonModel):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255, blank=True, null=True)
    memo = models.TextField(blank=True, null=True)

    customer = models.ForeignKey(
        "Customer",
        related_name="contacts",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    consignee = models.ForeignKey(
        "Consignee",
        related_name="contacts",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    carrier = models.ForeignKey(
        "Carrier",
        related_name="contacts",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


class Bank(CommonModel):
    name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=20)
    account_type = models.CharField(max_length=50, blank=True, null=True)
    memo = models.TextField(blank=True, null=True)

    customer = models.ForeignKey(
        "Customer",
        related_name="banks",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    consignee = models.ForeignKey(
        "Consignee",
        related_name="banks",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    carrier = models.ForeignKey(
        "Carrier", related_name="banks", on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.name

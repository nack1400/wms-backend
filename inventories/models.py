from django.db import models
from common.models import CommonModel
from partners.models import Customer
from handling_units.models import Pallet
from operations.models import Inbound, Outbound, Transfer
import datetime
import random
from enum import Enum


class Inventory(models.Model):
    STORAGE_TYPES = [
        ("freezer", "Freezer"),
        ("cooler", "Cooler"),
        ("dry", "Dry"),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    inbound = models.ForeignKey(Inbound, on_delete=models.CASCADE)
    transfer = models.ForeignKey(
        Transfer, on_delete=models.CASCADE, null=True, blank=True
    )

    pallet = models.ForeignKey(Pallet, on_delete=models.CASCADE)
    lot_number = models.CharField(max_length=50)

    lb_weight = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    kg_weight = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    location_type = models.CharField(max_length=10, choices=STORAGE_TYPES)
    pack_date = models.DateField(null=True, blank=True)
    expiration_date = models.DateField(null=True, blank=True)
    memo = models.TextField(null=True, blank=True)

    initial_quantity = models.PositiveIntegerField(default=0)
    current_quantity = models.PositiveIntegerField(default=0)
    picked_quantity = models.PositiveIntegerField(default=0)
    released_quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Inventory {self.id}"


class InventoryTransaction(CommonModel):
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    inbound = models.ForeignKey(
        Inbound, on_delete=models.CASCADE, null=True, blank=True
    )
    outbound = models.ForeignKey(
        Outbound, on_delete=models.CASCADE, null=True, blank=True
    )
    transfer = models.ForeignKey(
        Transfer, on_delete=models.CASCADE, null=True, blank=True
    )

    transaction_type = models.CharField(max_length=25)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Inventory Transaction {self.id}"

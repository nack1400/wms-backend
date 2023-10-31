from django.db import models
from django.utils import timezone
from partners.models import Customer
from common.models import CommonCreatedOnlyModel
from operations.models import Inbound, Outbound, Transfer


class Invoice(CommonCreatedOnlyModel):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    bill_date = models.DateField(default=timezone.now)
    due_date = models.DateField(null=True, blank=True)
    is_paid = models.BooleanField(default=False)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class StorageBilling(models.Model):
    BILLING_TYPES = [
        ("freezer", "Freezer"),
        ("cooler", "Cooler"),
        ("dry", "Dry"),
    ]

    code = models.CharField(max_length=20)
    billing_type = models.CharField(max_length=10, choices=BILLING_TYPES)
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    min_price = models.DecimalField(max_digits=10, decimal_places=2)
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True
    )
    description = models.TextField()

    def __str__(self):
        return self.code


class TaskBilling(models.Model):
    BILLING_TYPES = [
        ("freezer", "Freezer"),
        ("cooler", "Cooler"),
        ("dry", "Dry"),
    ]

    BILLING_UNITS = [
        ("pallet", "Pallet"),
        ("box", "Box"),
        ("manual", "Manual"),
    ]

    code = models.CharField(max_length=20)
    billing_unit = models.CharField(max_length=10, choices=BILLING_UNITS)
    billing_type = models.CharField(max_length=10, choices=BILLING_TYPES)
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    min_price = models.DecimalField(max_digits=10, decimal_places=2)
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True
    )
    description = models.TextField()

    def __str__(self):
        return self.code


class BillingItem(models.Model):
    storage_billing = models.ForeignKey(
        StorageBilling, on_delete=models.SET_NULL, null=True, blank=True
    )
    task_billing = models.ForeignKey(
        TaskBilling, on_delete=models.SET_NULL, null=True, blank=True
    )
    inbound = models.ForeignKey(
        Inbound, on_delete=models.SET_NULL, null=True, blank=True
    )
    outbound = models.ForeignKey(
        Outbound, on_delete=models.SET_NULL, null=True, blank=True
    )
    transfer = models.ForeignKey(
        Transfer, on_delete=models.SET_NULL, null=True, blank=True
    )
    invoice = models.ForeignKey(
        Invoice, on_delete=models.SET_NULL, null=True, blank=True
    )
    billing_unit = models.CharField(max_length=20)
    quantity = models.PositiveIntegerField()
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Billing Item #{self.pk}"

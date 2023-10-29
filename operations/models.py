from django.db import models
from common.models import CommonModel
from products.models import Product


class Inbound(CommonModel):
    quantity = models.PositiveIntegerField()
    received_date = models.DateField()

    def __str__(self):
        return f"Inbound {self.id} for {self.inbound_product.product.name}"


class InboundProduct(CommonModel):
    inbound = models.ForeignKey(
        Inbound,
        on_delete=models.CASCADE,
        related_name="inbound_products",
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name="inbound_products",
    )
    description = models.TextField(blank=True, null=True)
    manufacturing_date = models.DateField()
    expiration_date = models.DateField()

    def __str__(self):
        return f"Inbound Product for {self.product.name}"


class Outbound(CommonModel):
    quantity = models.PositiveIntegerField()
    shipped_date = models.DateField()

    def __str__(self):
        return f"Outbound {self.id} for {self.outbound_product.product.name}"


class OutboundProduct(CommonModel):
    outbound = models.ForeignKey(
        Outbound,
        on_delete=models.CASCADE,
        related_name="outbound_products",
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name="outbound_products",
    )
    description = models.TextField(blank=True, null=True)
    destination = models.CharField(max_length=255)

    def __str__(self):
        return f"Outbound Product for {self.product.name}"

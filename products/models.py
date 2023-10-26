from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save
from common.models import CommonModel


class Product(CommonModel):
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=50, unique=True, editable=False)
    packer = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    identification_code = models.CharField(max_length=100)
    memo = models.TextField(null=True, blank=True)
    category = models.ForeignKey(
        "categories.Category",
        related_name="products",
        on_delete=models.PROTECT,
    )

    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)
        category_sku = f"{self.category.key}-{self.category.sequence_number:05}"
        self.sku = f"{category_sku}"

    @receiver(pre_save, sender="products.Product")
    def generate_sku_and_update_category_sequence(sender, instance, *args, **kwargs):
        if not instance.sku:
            category = instance.category
            instance.sku = f"{category.key}-{str(category.sequence_number).zfill(5)}"
            category.sequence_number += 1
            category.save()

    def __str__(self):
        return self.name

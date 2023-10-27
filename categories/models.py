from django.db import models
from common.models import CommonModel
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Category(CommonModel):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(
        "self", related_name="children", null=True, blank=True, on_delete=models.CASCADE
    )
    key = models.CharField(max_length=100, unique=True, null=False, blank=False)
    sequence_number = models.IntegerField(default=1)
    billing_unit = models.CharField(max_length=50)
    level = models.PositiveIntegerField(default=0, editable=False)

    class Meta:
        ordering = ["level", "sequence_number"]

    def __str__(self):
        return self.name


@receiver(pre_save, sender=Category)
def set_category_level(sender, instance, *args, **kwargs):
    if not instance.parent:
        instance.level = 0
    else:
        instance.level = instance.parent.level + 1

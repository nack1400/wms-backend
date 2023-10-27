from django.db import models
from common.models import CommonTimeModel


class Pallet(CommonTimeModel):
    name = models.CharField(max_length=255)
    number = models.PositiveIntegerField(unique=True)


class PackagingUnit(CommonTimeModel):
    UNIT_CHOICES = (
        ("box", "Box"),
        ("pack", "Pack"),
        ("each", "Each"),
    )

    name = models.CharField(max_length=255)
    number = models.PositiveIntegerField(default=1)
    unit_type = models.CharField(max_length=50, choices=UNIT_CHOICES)
    pallet = models.ForeignKey(Pallet, on_delete=models.CASCADE)
from django.db import models
from common.models import CommonTimeModel
from warehouses.models import BinLocation
from simple_history.models import HistoricalRecords


class Pallet(CommonTimeModel):
    name = models.CharField(max_length=25)
    bin_location = models.ForeignKey(BinLocation, on_delete=models.PROTECT)
    history = HistoricalRecords()


class PackagingUnit(CommonTimeModel):
    UNIT_CHOICES = (
        ("box", "Box"),
        ("pack", "Pack"),
        ("each", "Each"),
    )

    name = models.CharField(max_length=25)
    unit_type = models.CharField(max_length=50, choices=UNIT_CHOICES)
    pallet = models.ForeignKey(Pallet, on_delete=models.CASCADE)
    history = HistoricalRecords()

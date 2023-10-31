from django.db import models
from common.models import CommonModel, CommonTimeModel
from simple_history.models import HistoricalRecords
from warehouses.models import Warehouse
from handling_units.models import Pallet, PackagingUnit


class Inspection(models.Model):
    name = models.CharField(max_length=25)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.PROTECT)
    history = HistoricalRecords()

    def __str__(self):
        return f"Inspection {self.id}"


class InspectionPallet(CommonTimeModel):
    inspection = models.ForeignKey(
        Inspection, on_delete=models.CASCADE, related_name="pallets"
    )
    pallet = models.ForeignKey(Pallet, on_delete=models.CASCADE)


class InspectionPackagingUnit(CommonTimeModel):
    inspection = models.ForeignKey(
        Inspection, on_delete=models.CASCADE, related_name="packaging_units"
    )
    packaging_unit = models.ForeignKey(PackagingUnit, on_delete=models.CASCADE)


class Inbound(CommonModel):
    name = models.CharField(max_length=25)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.PROTECT)
    inspection = models.ForeignKey(
        Inspection,
        on_delete=models.PROTECT,
        related_name="inbounds",
        null=True,
        blank=True,
    )
    history = HistoricalRecords()

    def __str__(self):
        return f"Inbound {self.id}"


class Outbound(CommonModel):
    name = models.CharField(max_length=25)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.PROTECT)
    inspection = models.ForeignKey(
        Inspection,
        on_delete=models.PROTECT,
        related_name="outbounds",
        null=True,
        blank=True,
    )
    history = HistoricalRecords()

    def __str__(self):
        return f"Outbound {self.id}"


class Transfer(CommonModel):
    name = models.CharField(max_length=25)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.PROTECT)
    inspection = models.ForeignKey(
        Inspection,
        on_delete=models.PROTECT,
        related_name="transfers",
        null=True,
        blank=True,
    )
    history = HistoricalRecords()

    def __str__(self):
        return f"Transfer {self.id}"

from django.db import models
from common.models import CommonModel
from simple_history.models import HistoricalRecords
from warehouses.models import Warehouse


class Inbound(CommonModel):
    name = models.CharField(max_length=25)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.PROTECT)
    history = HistoricalRecords()

    def __str__(self):
        return f"Inbound {self.id}"


class Outbound(CommonModel):
    name = models.CharField(max_length=25)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.PROTECT)
    history = HistoricalRecords()

    def __str__(self):
        return f"Outbound {self.id}"


class Transfer(CommonModel):
    name = models.CharField(max_length=25)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.PROTECT)
    history = HistoricalRecords()

    def __str__(self):
        return f"Outbound {self.id}"

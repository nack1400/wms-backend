from django.db import models
from common.models import CommonModel
from simple_history.models import HistoricalRecords


class Inbound(CommonModel):
    name = models.CharField(max_length=25)
    history = HistoricalRecords()

    def __str__(self):
        return f"Inbound {self.id}"


class Outbound(CommonModel):
    name = models.CharField(max_length=25)
    history = HistoricalRecords()

    def __str__(self):
        return f"Outbound {self.id}"


class Transfer(CommonModel):
    name = models.CharField(max_length=25)
    history = HistoricalRecords()

    def __str__(self):
        return f"Outbound {self.id}"

from django.db import models


class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    key = models.CharField(max_length=50)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class BinLocation(models.Model):
    LOCATION_TYPES = [
        ("freezer", "Freezer"),
        ("cooler", "Cooler"),
        ("dry", "Dry"),
    ]
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    location_type = models.CharField(max_length=10, choices=LOCATION_TYPES)
    key = models.CharField(max_length=50)
    is_available = models.BooleanField(default=True)
    is_multiple = models.BooleanField(default=False)
    width = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    depth = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"Bin Location {self.key} in {self.warehouse.name}"

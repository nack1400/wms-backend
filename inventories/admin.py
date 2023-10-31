from django.contrib import admin
from .models import Inventory, InventoryTransaction

admin.site.register(Inventory)
admin.site.register(InventoryTransaction)

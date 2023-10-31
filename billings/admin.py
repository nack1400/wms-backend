from django.contrib import admin
from .models import Invoice, StorageBilling, TaskBilling, BillingItem

admin.site.register(Invoice)
admin.site.register(StorageBilling)
admin.site.register(TaskBilling)
admin.site.register(BillingItem)

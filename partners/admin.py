from django.contrib import admin
from .models import Customer, Consignee, Carrier, CarrierAddress, Contact, Bank

admin.site.register(Customer)
admin.site.register(Consignee)
admin.site.register(Carrier)
admin.site.register(CarrierAddress)
admin.site.register(Contact)
admin.site.register(Bank)

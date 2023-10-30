from django.contrib import admin
from .models import Inbound, Outbound, Transfer
from simple_history.admin import SimpleHistoryAdmin


# @admin.register(Inbound)
# class InboundAdmin(SimpleHistoryAdmin):
#     list_display = ("quantity", "received_date")

admin.site.register(Inbound, SimpleHistoryAdmin)
admin.site.register(Outbound, SimpleHistoryAdmin)
admin.site.register(Transfer, SimpleHistoryAdmin)

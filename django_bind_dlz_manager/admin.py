from django_bind_dlz_manager import models
from django.contrib import admin


class DnsRecordAdmin(admin.ModelAdmin):
    search_fields = ('host', 'zone', 'data', 'type')
    list_filter = ('type', 'ttl')
    list_display = ('id', 'zone', 'host', 'type', 'data', 'ttl')


class XfrTableAdmin(admin.ModelAdmin):
    search_fields = ('zone', 'client')
    list_filter = ('zone', 'client')
    list_display = ('zone', 'client')


admin.site.register(models.DnsRecord, DnsRecordAdmin)
admin.site.register(models.XfrTable, XfrTableAdmin)

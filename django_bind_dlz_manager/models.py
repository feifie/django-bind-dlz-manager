from django.db import models


class DnsRecord(models.Model):
    id = models.AutoField(primary_key=True)
    zone = models.CharField(max_length=255, db_index=True)
    host = models.CharField(max_length=255, default='@', db_index=True)
    type = models.CharField(max_length=255, db_index=True)
    data = models.TextField(null=True, blank=True)
    ttl = models.IntegerField(default=86400)
    mx_priority = models.IntegerField(null=True, blank=True, default=None)
    refresh = models.IntegerField(null=True, blank=True, default=None)
    retry = models.IntegerField(null=True, blank=True, default=None)
    expire = models.IntegerField(null=True, blank=True, default=None)
    minimum = models.IntegerField(null=True, blank=True, default=None)
    serial = models.BigIntegerField(null=True, blank=True, default=None)
    resp_contact = models.CharField(max_length=255, null=True, blank=True, default=None)
    primary_ns = models.CharField(max_length=255, null=True, blank=True, default=None)

    class Meta:
        db_table = 'dns_records'
        index_together = ('zone', 'host')

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.type = self.type.upper()
        models.Model.save(self, force_insert=force_insert, force_update=force_update, using=using,
                          update_fields=update_fields)

    def __unicode__(self):
        return "%s %s %s %s" % (self.zone, self.ttl, self.type, self.data)

    def __str__(self):
        return "%s %s %s %s" % (self.zone, self.ttl, self.type, self.data)


class XfrTable(models.Model):
    zone = models.CharField(max_length=255, db_index=True)
    client = models.CharField(max_length=255, db_index=True)

    class Meta:
        db_table = 'xfr_table'
        index_together = ('zone', 'client')

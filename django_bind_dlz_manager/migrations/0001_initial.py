# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DnsRecord',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('zone', models.CharField(max_length=255, db_index=True)),
                ('host', models.CharField(default=b'@', max_length=255, db_index=True)),
                ('type', models.CharField(max_length=255, db_index=True)),
                ('data', models.TextField(null=True, blank=True)),
                ('ttl', models.IntegerField(default=86400)),
                ('mx_priority', models.IntegerField(default=None, null=True, blank=True)),
                ('refresh', models.IntegerField(default=None, null=True, blank=True)),
                ('retry', models.IntegerField(default=None, null=True, blank=True)),
                ('expire', models.IntegerField(default=None, null=True, blank=True)),
                ('minimum', models.IntegerField(default=None, null=True, blank=True)),
                ('serial', models.BigIntegerField(default=None, null=True, blank=True)),
                ('resp_contact', models.CharField(default=None, max_length=255, null=True, blank=True)),
                ('primary_ns', models.CharField(default=None, max_length=255, null=True, blank=True)),
            ],
            options={
                'db_table': 'dns_records',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='XfrTable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zone', models.CharField(max_length=255, db_index=True)),
                ('client', models.CharField(max_length=255, db_index=True)),
            ],
            options={
                'db_table': 'xfr_table',
            },
            bases=(models.Model,),
        ),
        migrations.AlterIndexTogether(
            name='xfrtable',
            index_together=set([('zone', 'client')]),
        ),
        migrations.AlterIndexTogether(
            name='dnsrecord',
            index_together=set([('zone', 'host')]),
        ),
    ]

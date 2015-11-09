from __future__ import absolute_import

from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Returns a properly config for Bind9'

    def handle(self, *args, **options):
        for db in settings.DATABASES:
            data = settings.DATABASES[db]
            if 'DLZ_NAME' not in data:
                data['DLZ_NAME'] = db
            if data['ENGINE'] == 'django.db.backends.postgresql_psycopg2':
                self.stdout.write("""dlz "%(DLZ_NAME)s" {
    database "postgres 2
        {host=%(HOST)s port=%(PORT)s dbname=%(NAME)s user=%(USER)s password=%(PASSWORD)s}
        {SELECT zone FROM dns_record WHERE zone = '$zone$'}
        {SELECT ttl, type, mx_priority,
        case when lower(type)='txt' then '\\"' || data || '\\"' else data end AS data
        FROM dns_record
        WHERE zone = '$zone$' AND host = '$record$' AND type <> 'SOA' AND type <> 'NS'}
        {SELECT ttl, type, data, primary_ns, resp_contact, serial, refresh, retry, expire, minimum
        FROM dns_record
        WHERE zone = '$zone$' AND (type = 'SOA' OR type='NS')}
        {SELECT ttl, type, host, mx_priority,
        case when lower(type)='txt' then '\\"' || data || '\\"' else data end AS data,
        resp_contact, serial, refresh, retry, expire, minimum
        FROM dns_record
        WHERE zone = '$zone$' AND type <> 'SOA' AND type <> 'NS'}
        {SELECT zone FROM dns_xfr where zone='$zone$' AND client = '$client$'}";
};""" % data)
            elif data['ENGINE'] == 'django.db.backends.mysql':
                self.stdout.write("""dlz "%(DLZ_NAME)s" {
    database "mysql
        {host=%(HOST)s port=%(PORT)s dbname=%(NAME)s user=%(USER)s password=%(PASSWORD)s}
        {SELECT zone FROM dns_records WHERE zone = '$zone$'}
        {SELECT ttl, type, mx_priority,
        IF(type = 'TXT', CONCAT('\\"',data,'\\"'), data) AS data
        FROM dns_records
        WHERE zone = '$zone$' AND host = '$record$' AND type <> 'SOA' AND type <> 'NS'}
        {SELECT ttl, type, data, primary_ns, resp_person, serial, refresh, retry, expire, minimum
        FROM dns_records
        WHERE zone = '$zone$' AND (type = 'SOA' OR type='NS')}
        {SELECT ttl, type, host, mx_priority,
        IF(type = 'TXT', CONCAT('\\"',data,'\\"'), data) AS data,
        resp_person, serial, refresh, retry, expire, minimum
        FROM dns_records
        WHERE zone = '$zone$' AND type <> 'SOA' AND type <> 'NS'}
        {SELECT zone FROM xfr_table where zone='$zone$' AND client = '$client$'}";
};""" % data)
            else:
                self.stderr.write("%(DLZ_NAME)s \"%(ENGINE)s\" not supported" % data)

# django-bind-dlz-manager
This tool allow to manager a [bind9](https://www.isc.org/downloads/bind/)
with [DLZ](http://bind-dlz.sourceforge.net/) administration panel with 
[Django](https://www.djangoproject.com/) as frontend.

Install
=======
Add 'django_bind_dlz_manager' in to INSTALLED_APPS:
```
INSTALLED_APPS = (
    ...
    'django_bind_dlz_manager',
    ...
)
```

If you need a local Bind9 you can run [compile_bind9.sh](script/compile_bind9.sh) based on [post in Ubuntu forum](http://ubuntuforums.org/showthread.php?t=1867237)
for compile [bind9](https://www.isc.org/downloads/bind/) with [DLZ](http://bind-dlz.sourceforge.net/) support.

See [DLZ best practices](http://bind-dlz.sourceforge.net/best_practices.html) for configure your DNS server.

Use ```python manage.py bind9_conf``` to generete the config file for add to ```/etc/bind/named.conf```.

```
python manager.py bind9_conf >> /etc/bind/named.conf
```

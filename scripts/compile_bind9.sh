#!/usr/bin/env bash
# See more info at: http://ubuntuforums.org/showthread.php?t=1867237

sudo apt-get install bind9 bind9utils -y -qq
sudo apt-get remove bind9 -y -qq
sudo apt-get build-dep bind9 -y -qq

# PostgreSQL Database
sudo apt-get install libpq-dev -y -qq
# sudo apt-get install postgresql-9.4
# MySQL Database
sudo apt-get install libmysqlclient-dev mysql-client -y -qq
# sudo apt-get install mysql-server

apt-get source bind9
cd bind9*
# Use ./configure --help for see all options
CONF_PATH="--with-randomdev=/dev/random --prefix=/usr --sysconfdir=/etc/bind --localstatedir=/var --mandir=/usr/share/man --infodir=/usr/share/info --with-openssl=/usr --with-gssapi=/usr --with-geoip=/usr"
CONF_ENABLE="--with-libtool --with-gnu-ld --enable-threads --enable-largefile --enable-shared --enable-static --enable-rrl --enable-newstats --enable-ipv6 --enable-filter-aaaa"
CONF_DLZ="--with-dlz-postgres=yes --with-dlz-mysql=yes --with-dlz-bdb=no --with-dlz-ldap=no --with-dlz-stub=no --with-dlz-filesystem=no"
CONF_CFLAG="CFLAGS=-fno-strict-aliasing -fno-delete-null-pointer-checks -DDIG_SIGCHASE -O2"
CONF_LDFLAGS="LDFLAGS=-Wl,-Bsymbolic-functions"
CONF_CPPFLAGS="CPPFLAGS="
./configure $CONF_PATH $CONF_ENABLE --with-gnu-ld $CONF_DLZ "$CONF_CFLAG" "$CONF_LDFLAGS" "$CONF_CPPFLAGS"
make
sudo make install

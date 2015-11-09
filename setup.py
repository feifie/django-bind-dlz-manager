from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup

import django_bind_dlz_manager as meta

setup(name='django-bind-dlz-manager',
      description='Bind9 DLZ Manager',
      version='.'.join(map(str, meta.__version__)),
      author=meta.__author__,
      author_email=meta.__contact__,
      url=meta.__homepage__,
      license=meta.__license__,
      keywords='django dns bind9 dlz',
      requires=['django'],
      platforms=['any'],
      classifiers=[
          "Framework :: Django",
          "Environment :: Web Environment",
          "Intended Audience :: Developers",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Topic :: Internet :: Name Service (DNS)",
          "Topic :: System :: Systems Administration",
          "Topic :: Software Development :: Libraries :: Application Frameworks",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      packages=['django_bind_dlz_manager', ])

import os
import sys
path='/var/www/vpn.mrlin.tk'
sys.path.append('/root/django-trunk/django/')
sys.path.append('/root/django-trunk/')
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

"""
WSGI config for tst_1160fc36_56ce_496_135 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "tst_1160fc36_56ce_496_135.settings"
)

application = get_wsgi_application()

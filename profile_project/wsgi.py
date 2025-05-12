"""
WSGI config for profile_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'profile_project.settings')

# Correct order:
application = get_wsgi_application()  # 1. Get Django app first
application = WhiteNoise(application)  # 2. Then wrap with WhiteNoise

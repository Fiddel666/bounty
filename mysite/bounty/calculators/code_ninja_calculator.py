# importing django
import os
import django

# setting django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

# import django's DB API
from bounty.models import *






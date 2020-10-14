import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from bounty.scraper.get_html import scrap
from bounty.models import *

data = scrap()

for usr in data:
	u = users(user = usr.name, belt = usr.rank, warning = usr.warning)
	print(u.id, u.user, u.belt, u.warning)
	u.save()
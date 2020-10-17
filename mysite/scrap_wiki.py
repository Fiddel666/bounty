# importing django and django settings
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

# import DATA and django's DB API
from bounty.scraper.get_html import scrap
from bounty.models import *

data = scrap()

# save to DB using django's DB API(models)
for usr in data:
	u = users(user = usr.name, belt = usr.rank, warning = usr.warning)
	print(u.id, u.user, u.belt, u.warning)
	u.save()
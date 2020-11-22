# importing django
import os
import django

# setting django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

# import scrapers and django's DB API
from bounty.scraper import get_users, get_challenges, get_scores
from bounty.models import *

def users_scrap():
	users = get_users.scrap()

	# save to DB using django's DB API(models)
	for usr in users:
		#print(usr.house)
		h, created = house.objects.get_or_create(name=usr.house)
		#print(h.name)
		u, created = code_ninja.objects.get_or_create(nick=usr.name, warning=usr.warning, house=h)
		#print(u.nick, u.warning, u.house.name)
		u.save()

def challenges_scrap():
	challs = get_challenges.scrap()
	#print('start')
	# save to DB using django's DB API(models)
	for category in challs:
		#print(challs[category])
		for chall in challs[category]:
			c, created = challenges.objects.get_or_create(	
							name=chall.name, points=chall.points, category=category,
							description=chall.description
						  )
			print(c.name, c.points, c.category, c.description)
			print("-----------------------------------------")
			c.save()

def score_scrap():
	changed_names = {
						"shot4shot": "headshot",
						"Cuphead": "hatsyl",
						"cuphead": "hatsyl",
						"Hari": "hari",
						"Blanco": "blanco"
					}
	scores = get_scores.scrap()
	#print(scores)
	for category in scores:
		#print(category, scores[category])
		#print("------------------------------------------------")
		
		for chall in scores[category]:
			#print(category, chall)
			c = challenges.objects.filter(name=chall, category=category).first()
			if(not c):
				continue
			#print((c.category, c.name, c.points)) if c else print(chall, " does not exist")
			
			for user in scores[category][chall]:
				#print(category, chall, user)
				if(user in changed_names):
					user = changed_names[user]
					#print(user)
				
				usr = code_ninja.objects.filter(nick=user).first()
				if(not usr):
					#print(user)
					continue
				#print(usr.id, usr.nick) if usr else print(user, " does not exist-------------------in ", c.name)
				
				s, created = score.objects.get_or_create(userID=usr, challengesID=c)
				#print(s.userID.nick, s.challengesID.name)
				#print("-----------------------------------------")
				s.save()

#users_scrap()
#challenges_scrap()
score_scrap()




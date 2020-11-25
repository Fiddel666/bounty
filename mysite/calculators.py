# importing django
import os
import django

# setting django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

# import django's DB API
from bounty.models import *

from collections import defaultdict

def code_ninja_calc():
	users = code_ninja.objects.all()
	titles = {"C":samurai_c, "Java":coffe_makers, "Python":python_slayer}
	#print(titles["c"])
	
	for user in users:
		points = defaultdict(int)
		total = 0
		scores = score.objects.filter(userID=user.id)
		
		for scr in scores:
			#print(scr.userID.nick, scr.challengesID.name)
			#print("------------------------------------------------------------------")
			points[scr.challengesID.category] += int(scr.challengesID.points)
			total += int(scr.challengesID.points)
			#print(points[scr.challengesID.category])
		
		for point in points:
			#print(point)
			if point in titles:
				#print(titles[point])
				player, created = titles[point].objects.get_or_create(userID=user)
				player.total_score = points[point]
				player.save()
				print(player.id, player.total_score, player.userID.nick)
		
		#print(user.nick, dict(points), total)
		user.rank = str(total/10)
		user.save()

#def samurai_c_calc():
#	users = code_ninja.objects.all()

code_ninja_calc()

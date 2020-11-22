from django.db import models
from django.contrib.auth import get_user_model

auth_user = get_user_model()
# Create your models here.

class house(models.Model):
	name = models.CharField(max_length=20)

class code_ninja(models.Model):
	userID = models.OneToOneField(	
									auth_user,
									on_delete=models.CASCADE,
									unique=True,
									null=True
								)
	nick = models.CharField(max_length=20, unique=True)
	rank = models.CharField(max_length=20)
	belt = models.CharField(max_length=20)
	status = models.CharField(max_length=20)
	warning = models.IntegerField(default=0)
	house = models.ForeignKey(
								house,
								on_delete=models.CASCADE
							)

class challenges(models.Model):
	name = models.CharField(max_length=100)
	points = models.CharField(max_length=20, default=0)
	category = models.CharField(max_length=20)
	mentor = models.ForeignKey(	
								code_ninja,
								on_delete=models.CASCADE,
								null=True
							)
	description = models.CharField(max_length=1000)
	
	class Meta:
		unique_together = ["name", "points", "category", "description"]

class score(models.Model):
	userID = models.ForeignKey(	
								code_ninja,
								on_delete=models.CASCADE
							)
	challengesID = models.ForeignKey(	
								challenges,
								on_delete=models.CASCADE
							)

class samurai_c(models.Model):
	userID = models.ForeignKey(	
								code_ninja,
								on_delete=models.CASCADE
							)
	total_score = models.IntegerField(default=0)

class game_of_pwns(models.Model):
	userID = models.ForeignKey(	
								code_ninja,
								on_delete=models.CASCADE
							)
	total_score = models.IntegerField(default=0)

class coffe_makers(models.Model):
	userID = models.ForeignKey(	
								code_ninja,
								on_delete=models.CASCADE
							)
	total_score = models.IntegerField(default=0)

class python_slayer(models.Model):
	userID = models.ForeignKey(	
								code_ninja,
								on_delete=models.CASCADE
							)
	total_score = models.IntegerField(default=0)






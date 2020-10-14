from django.db import models

# Create your models here.

class house(models.Model):
	name = models.CharField(max_length=20)

class users(models.Model):
	user = models.CharField(max_length=20)
	level = models.IntegerField(default=0)
	belt = models.CharField(max_length=20)
	house = models.ForeignKey(house, on_delete=models.CASCADE, null=True)
	status = models.CharField(max_length=20)
	warning = models.IntegerField(default=0)

class scores(models.Model):
	topic = models.CharField(max_length=20)
	score = models.IntegerField(default=0)

class code_wars(models.Model):
	kyu = models.IntegerField(default=0)
	color = models.CharField(max_length=20)
	top_precentage = models.CharField(max_length=20)
	place = models.IntegerField(default=0)

class challenges(models.Model):
	name = models.CharField(max_length=20)
	topic = models.CharField(max_length=20)
	mentor = models.CharField(max_length=20)
	description = models.CharField(max_length=20)




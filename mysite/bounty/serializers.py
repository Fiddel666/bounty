from rest_framework import serializers
from .models import *

class houseSerializer(serializers.ModelSerializer):
    class Meta:
        model = house
        fields = ('id', 'name')

class usersSerializer(serializers.ModelSerializer):
	house = serializers.CharField(source='house.name')
	
	class Meta:
		model = users
		fields = ('id', 'user', 'level', 'belt', 'status', 'warning', 'house')

class scoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = scores
        fields = ('id', 'topic', 'score')

class code_warsSerializer(serializers.ModelSerializer):
    class Meta:
        model = code_wars
        fields = ('id', 'kyu', 'color', 'top_precentage', 'place')

class challengesSerializer(serializers.ModelSerializer):
    class Meta:
        model = challenges
        fields = ('id', 'name', 'topic', 'mentor', 'description')


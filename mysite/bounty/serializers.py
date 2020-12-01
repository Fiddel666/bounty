from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class houseSerializer(serializers.ModelSerializer):
    class Meta:
        model = house
        fields = ('id', 'name')
		
class code_ninjaSerializer(serializers.ModelSerializer):
	#house = serializers.PrimaryKeyRelatedField(null=True, source='house')
	#house = serializers.CharField(source='house.name')
	
	class Meta:
		model = code_ninja
		fields = ('id', 'userID', 'nick', 'rank', 'belt', 'status', 'warning', 'house')

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id', 'username', 'password']
	
	# creat method will hash the password
	def create(self, validated_data):
		user = User.objects.create_user(**validated_data)
		return user

class challengesSerializer(serializers.ModelSerializer):
    class Meta:
        model = challenges
        fields = ('id', 'name', 'points', 'category', 'mentor', 'description')

class scoreSerializer(serializers.ModelSerializer):
	challenge = serializers.CharField(source='challengesID.name', read_only=True)
	user = serializers.CharField(source='userID.nick', read_only=True)
	
	class Meta:
		model = score
		fields = ('id', 'user', 'challenge')




from .models import *
from .serializers import *
from rest_framework import generics, viewsets
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.http import JsonResponse
#import scrap_wiki.py

class houseListCreate(generics.ListCreateAPIView):
	queryset = house.objects.all()
	serializer_class = houseSerializer

class code_ninjaListCreate(generics.ListCreateAPIView):
	queryset = code_ninja.objects.all()
	serializer_class = code_ninjaSerializer

class scoreListCreate(generics.ListCreateAPIView):
	#queryset = score.objects.all()
	serializer_class = scoreSerializer
	def get_queryset(self):
		print(self.request.user)
		return score.objects.filter(userID = self.request.user.id)

class challengesListCreate(generics.ListCreateAPIView):
	queryset = challenges.objects.all()
	serializer_class = challengesSerializer

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

def log_in_view(request):
	# use .get() to not rise error/exception
	username = request.POST.get('username')
	password = request.POST.get('password')
	print(username, password)
	user = authenticate(request, username=username, password=password)
	print(user)
	
	if user is not None:
		login(request, user)	# sets session ID to cookies
		log_in = "OK"
	else:
		log_in = "NO"
	
	return JsonResponse({"login": log_in})

def log_out_view(request):
	logout(request)
	return JsonResponse({"logout": True})





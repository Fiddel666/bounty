from .models import *
from .serializers import *
from rest_framework import generics


class houseListCreate(generics.ListCreateAPIView):
    queryset = house.objects.all()
    serializer_class = houseSerializer

class usersListCreate(generics.ListCreateAPIView):
    queryset = users.objects.all()
    serializer_class = usersSerializer

class scoresListCreate(generics.ListCreateAPIView):
    queryset = scores.objects.all()
    serializer_class = scoresSerializer

class code_warsListCreate(generics.ListCreateAPIView):
    queryset = code_wars.objects.all()
    serializer_class = code_warsSerializer

class challengesListCreate(generics.ListCreateAPIView):
    queryset = challenges.objects.all()
    serializer_class = challengesSerializer

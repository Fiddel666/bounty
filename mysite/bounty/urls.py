from django.urls import path
from . import views


urlpatterns = [
	path('api/house/', views.houseListCreate.as_view() ),
	path('api/users/', views.usersListCreate.as_view() ),
	path('api/scores/', views.scoresListCreate.as_view() ),
	path('api/code_wars/', views.code_warsListCreate.as_view() ),
	path('api/challenges/', views.challengesListCreate.as_view() ),
]
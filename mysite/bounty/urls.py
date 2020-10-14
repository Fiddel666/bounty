from django.urls import path
from . import views
#from django.conf import settings
#from django.conf.urls.static import static

'''
urlpatterns = [
	path('', views.index, name='index'),
	path('<int:score_id>/', views.detail, name='detail'),
	path('<int:score_id>/results/', views.results, name='results'),
	path('<int:score_id>/change/', views.change, name='change'),
]
'''

urlpatterns = [
	path('api/house/', views.houseListCreate.as_view() ),
	path('api/users/', views.usersListCreate.as_view() ),
	path('api/scores/', views.scoresListCreate.as_view() ),
	path('api/code_wars/', views.code_warsListCreate.as_view() ),
	path('api/challenges/', views.challengesListCreate.as_view() ),
]
from django.urls import path
from . import views
from rest_framework import routers
from django.conf.urls import include

# must use router on view set
router = routers.DefaultRouter()
router.register('user', views.UserViewSet)

urlpatterns = [
	path('api/house/', views.houseListCreate.as_view() ),
	path('api/users/', views.code_ninjaListCreate.as_view() ),
	path('', include(router.urls) ),
	path('api/scores/', views.scoreListCreate.as_view() ),
	path('api/challenges/', views.challengesListCreate.as_view() ),
	path('login/', views.log_in_view ),
]
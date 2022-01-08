from django.urls import path, include
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from Film import views


router = DefaultRouter()

router.register('genres', views.GenreViewSet)

app_name = 'Film'

urlpatterns = [
    path('', include(router.urls))
]
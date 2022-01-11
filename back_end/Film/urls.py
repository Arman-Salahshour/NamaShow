from django.urls import path, include
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from Film import views


router = DefaultRouter()

router.register('genre', views.GenreViewSet)
router.register('celebrity', views.CelebrityViewSet)
router.register('film', views.FilmViewSet)
router.register('video', views.VideoViewSet)

app_name = 'Film'

urlpatterns = [
    path('', include(router.urls)),
    path('film/<int:filmID>', views.RetrieveFilmViewSet.as_view(), name='retFilm')
]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Film import views


router = DefaultRouter()

router.register('genre', views.GenreViewSet)
router.register('celebrity', views.CelebrityViewSet)
router.register('film', views.FilmViewSet)
router.register('film/create', views.FilmCreateViewSet)
router.register('video', views.VideoViewSet)

app_name = 'Film'

urlpatterns = [
    path('', include(router.urls)),
    path('film/<int:filmID>', views.FilmRetrieveViewSet.as_view(), name='retFilm'),
    path('genre/<int:genreID>', views.GenreRetrieveViewSet.as_view(), name='retGenre'),
    path('video/<int:videoID>', views.VideoRetrieveViewSet.as_view(), name='retVideo'),
    path('celebrity/<int:celebID>', views.CelebrityRetrieveViewSet.as_view(), name='retCeleb'),
]
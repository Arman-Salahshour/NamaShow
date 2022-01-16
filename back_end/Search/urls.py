from django.urls import path
from .views import SearchFilm

urlpatterns=[
    path('',SearchFilm.as_view())
]
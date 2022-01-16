from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('User.urls')),
    path('api/film/', include('Film.urls')),
    path('api/search', include('Search.urls'))
]

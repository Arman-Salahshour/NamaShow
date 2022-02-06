from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('User.urls')),
    path('api/film/', include('Film.urls')),
    path('api/search/', include('Search.urls')),
    path('api/post/', include('Post.urls')),
    path('api/subscription/', include('Subscription.urls')),
]

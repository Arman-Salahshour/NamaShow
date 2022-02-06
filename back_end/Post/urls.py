from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Post import views


router = DefaultRouter()

router.register('', views.PostViewSet)

app_name = 'Post'

urlpatterns = [
    path('', include(router.urls)),
    path('<int:postID>/', views.PostRetrieveViewSet.as_view(), name='retPost'),
]
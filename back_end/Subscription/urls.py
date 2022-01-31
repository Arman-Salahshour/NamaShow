from django.urls import path, include
from Subscription import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('', views.SubsciptionViewSet)

app_name = 'Subscription'

urlpatterns = [
    path('', include(router.urls)),
    path('<int:subID>/', views.SubscriptionRetrieveViewSet.as_view(), name='retSub'),
    path('buy/', views.SubPurchaseView.as_view(), name='buySub'),
]

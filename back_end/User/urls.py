from django.urls import path
from User import views


app_name = 'User'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.UserTokenView.as_view(), name='token'),
    path('update/', views.ManageUserView.as_view(), name='update'),
    path('pay/', views.PaymentView.as_view(), name='pay'),
]

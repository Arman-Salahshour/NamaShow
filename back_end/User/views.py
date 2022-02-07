from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from rest_framework import generics, viewsets
from Core.models import Payment
from User.serializers import UserInfoSerializer, UserSerializer, UserTokenSerializer \
                           , PaymentSerializer, UserUpdateSerializer, MyFilmsSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.


# Creates a user
class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    authentication_classes = ()


# User Login
class UserTokenView(TokenObtainPairView):
    serializer_class = UserTokenSerializer

    
# Updating user information
class ManageUserView(generics.UpdateAPIView):
    serializer_class = UserUpdateSerializer

    def get_object(self):
        return self.request.user


# Retrieving authenticated user's information
class UserInfoViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserInfoSerializer

    def get_queryset(self):
        uID = getattr(self.request.user,'userID')
        return get_user_model().objects.filter(userID=uID)

    def get_object(self):
        uID = getattr(self.request.user,'userID')
        return self.queryset.filter(userID=uID)


# To make payments
class PaymentView(generics.CreateAPIView):
    serializer_class = PaymentSerializer

    def get_queryset(self):
        return Payment.objects.all()


# User films' List
class MyFilmsViewset(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = MyFilmsSerializer

    def get_queryset(self):
        uID = getattr(self.request.user,'userID')
        return get_user_model().objects.filter(userID=uID)

    def get_object(self):
        uID = getattr(self.request.user,'userID')
        return self.queryset.filter(userID=uID)
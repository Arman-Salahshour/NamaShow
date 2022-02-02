from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from rest_framework import generics, viewsets
from rest_framework.generics import RetrieveAPIView
from Core.models import Payment, Film
from User.serializers import UserInfoSerializer, UserSerializer, UserTokenSerializer \
                           , PaymentSerializer, UserUpdateSerializer, FilmListSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    authentication_classes = ()

class UserTokenView(TokenObtainPairView):
    serializer_class = UserTokenSerializer

    
class ManageUserView(generics.UpdateAPIView):
    serializer_class = UserUpdateSerializer

    def get_object(self):
        return self.request.user

class UserInfoViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserInfoSerializer

    def get_queryset(self):
        uID = getattr(self.request.user,'userID')
        return get_user_model().objects.filter(userID=uID)

    def get_object(self):
        uID = getattr(self.request.user,'userID')
        return self.queryset.filter(userID=uID)

class PaymentView(generics.CreateAPIView):
    serializer_class = PaymentSerializer

    def get_queryset(self):
        return Payment.objects.all()


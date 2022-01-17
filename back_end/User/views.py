from django.contrib.auth import get_user_model
from rest_framework import generics, viewsets, mixins
from Core.models import Payment
from User.serializers import UserInfoSerializer, UserSerializer, UserTokenSerializer, PaymentSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import permissions


# Create your views here.


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

class UserTokenView(TokenObtainPairView):
    serializer_class = UserTokenSerializer

    
class ManageUserView(generics.UpdateAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

class UserInfoViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserInfoSerializer

    def get_object(self):
        uID = getattr(self.request.user,'userID')
        return self.queryset.filter(userID=uID)

class PaymentView(generics.CreateAPIView):
    serializer_class = PaymentSerializer

    def get_queryset(self):
        return Payment.objects.all()

    
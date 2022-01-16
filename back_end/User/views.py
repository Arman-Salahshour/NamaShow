from rest_framework import generics
from Core.models import Payment
from User.serializers import UserSerializer, UserTokenSerializer, PaymentSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes, authentication_classes


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


class PaymentView(generics.CreateAPIView):
    serializer_class = PaymentSerializer

    def get_queryset(self):
        return Payment.objects.all()

    
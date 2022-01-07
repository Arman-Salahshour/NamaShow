from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from User import serializers
from User.serializers import UserSerializer, AuthTokenSerializer

# Create your views here.


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer

class CreateTokenView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
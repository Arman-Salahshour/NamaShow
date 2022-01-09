from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.serializers import Serializer
from rest_framework.settings import api_settings
from User.serializers import UserSerializer, AuthTokenSerializer, TokenSerializer
from rest_framework.authtoken.models import Token as DefaultTokenModel
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

    def get_queryset(self):
        return self.request.user

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        return get_token_response(user)


class ManageUserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user



# Extra Methods
def get_token_response(user):
    serializer_class = TokenSerializer
    token, _ = DefaultTokenModel.objects.get_or_create(user=user)
    serializer = serializer_class(instance=token)
    return Response(serializer.data, status=status.HTTP_200_OK)
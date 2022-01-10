from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.serializers import Serializer
from rest_framework.settings import api_settings
from User.serializers import UserSerializer, AuthTokenSerializer
from rest_framework.authtoken.models import Token as DefaultTokenModel
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status
import jwt

# Create your views here.


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

    def get_queryset(self):
        return self.request.user

    def post(self, request):
        usernameIN = request.data['username']
        passwordIN = request.data['password']

        user = get_user_model().objects.filter(username=usernameIN).first()

        if user is None:
            user = get_user_model().objects.filter(email=usernameIN).first()
        
        if user is None:
            raise AuthenticationFailed('No user with this username/email!') 
        
        if not user.check_password(passwordIN):
            raise AuthenticationFailed('Input password is incorrect!')

        payload = {
            'id': user.userID,
            'username': user.username,
            'email': user.email,
            'name': user.name,
            'balance': user.balance,
            'isActivated': user.emailActivation
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response



    """def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        return get_token_response(user)"""


class ManageUserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user



# Extra Methods
"""def get_token_response(user):
    serializer_class = TokenSerializer
    token, _ = DefaultTokenModel.objects.get_or_create(user=user)
    serializer = serializer_class(instance=token)
    return Response(serializer.data, status=status.HTTP_200_OK)"""
from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password', 'name')
        extra_kwargs = {
            'password': {'write_only':True, 'min_length':8},
            'username': {'min_length':8}
            }

    def create(self, validatedData):
        return get_user_model().objects.createUser(**validatedData)


class AuthTokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(trim_whitespace=False)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username= username,
            password= password
        )
        if not user:
            msg = 'Authentication Failed.'
            raise serializers.ValidationError(msg, code='authentication')

        attrs['user'] = user
        return attrs
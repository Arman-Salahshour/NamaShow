from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from rest_framework.authtoken.models import Token as DefaultTokenModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username','email', 'password', 'name', 'balance', 'emailActivation', 'isSuspended')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}
        read_only_fields = ('balance', 'isSuspended', 'emailActivation')

    def create(self, validated_data):
        return get_user_model().objects.createUser(**validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


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


class TokenSerializer(serializers.ModelSerializer):   
    user = UserSerializer()
    class Meta:
        model = DefaultTokenModel
        fields = ('key', 'user',)
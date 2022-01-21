from django.contrib.auth import get_user_model
from django.http import request
from rest_framework import serializers
from rest_framework.authtoken.models import Token as DefaultTokenModel
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenObtainSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from Core.models import Payment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('userID', 'username','email', 'password', 'name', 'balance', 'emailActivation', 'isSuspended')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}
        read_only_fields = ('userID', 'balance', 'isSuspended', 'emailActivation')

    def create(self, validated_data):
        return get_user_model().objects.createUser(**validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'name',)
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8,'required': False,},
                        'email': {'required': False,},
                        'name': {'required': False,},}

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user



class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('userID', 'username','email', 'name', 'balance', 'emailActivation', 'isSuspended')
        read_only_fields = ('userID', 'username','email', 'name', 'balance', 'emailActivation', 'isSuspended')


class UserTokenSerializer(TokenObtainSerializer):
    @classmethod
    def get_token(cls, user):
        token = RefreshToken.for_user(user)
        token['userID'] = user.userID
        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['access'] = str(refresh.access_token)

        return data


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('user', 'amount',)
        read_only_fields = ('user',)

    def create(self, validated_data):
        request = self.context.get("request")
        user = request.user
        uID = getattr(user,'userID')
        uBalance = getattr(user, 'balance')
        amount = int(validated_data['amount'])
        uBalance = uBalance + amount
        get_user_model().objects.filter(userID=uID).update(balance=uBalance)
        validated_data['user'] = user
        

        return super().create(validated_data)
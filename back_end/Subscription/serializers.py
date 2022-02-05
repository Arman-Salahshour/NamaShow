from django.contrib.auth import get_user_model
from django.forms import ValidationError
from rest_framework import serializers
from Core.models import SubPurchase, Subscription
import datetime


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ('__all__')
        read_only_fields = ('subID', 'salePercentage', 'saleExpiration')


class SubscriptionRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ('__all__')
        read_only_fields = ('subID',)


class SubPurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubPurchase
        fields = ('user', 'subscription', 'price','dateOf')
        read_only_fields = ('user', 'price', 'dateOf')

    def create(self, validated_data):
        validated_data['dateOf'] = datetime.datetime.now()

        request = self.context.get("request")
        user = request.user
        validated_data['user'] = user
        uID = getattr(user,'userID')
        
        latestSub = SubPurchase.objects.filter(user=user).order_by('dateOf').last()
        if(latestSub):
            latestDate = getattr(latestSub, 'dateOf')
            expDate = latestDate + datetime.timedelta(days=30)
            print(datetime.datetime.now())
            if(datetime.datetime.now() < expDate):
                raise ValidationError('Already have a subscription.', code='already-subbed')

        subscription = validated_data['subscription']
        price = int(getattr(subscription,'price'))
        validated_data['price'] = price
        balance = int(getattr(user, 'balance'))
        if(price>balance):
            raise ValidationError('Not enough balance.', code='low_balance')
        balance = balance - price
        get_user_model().objects.filter(userID=uID).update(balance=balance)        

        return super().create(validated_data)
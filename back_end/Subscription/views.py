from rest_framework.permissions import AllowAny
from rest_framework import generics, viewsets, mixins
from Core.models import Payment, SubPurchase, Subscription
from Subscription.serializers import SubPurchaseSerializer, SubscriptionSerializer, SubscriptionRetrieveSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import RetrieveUpdateDestroyAPIView

# Create your views here.


class SubsciptionViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = SubscriptionSerializer
    authentication_classes = ()
    permission_classes = (AllowAny,)
    queryset = Subscription.objects.all()
    pagination_class = PageNumberPagination

    def get_queryset(self):
        return self.queryset
    
    def perform_create(self, serializer):
        serializer.save()


class SubscriptionRetrieveViewSet(RetrieveUpdateDestroyAPIView):
    serializer_class = SubscriptionRetrieveSerializer
    authentication_classes = ()
    permission_classes = (AllowAny,)
    queryset = Subscription.objects.all()
    lookup_field = 'subID'

    def get_queryset(self):
        return self.queryset


class SubPurchaseView(generics.CreateAPIView):
    serializer_class = SubPurchaseSerializer

    def get_queryset(self):
        return SubPurchase.objects.all()
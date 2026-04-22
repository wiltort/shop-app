from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView, Response

from orders.api.v1.serializers import ItemSerializer
from orders.models import Item
from orders.services import stripe_service


class ItemView(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemBuyView(APIView):
    def get(self, request, *args, **kwargs):
        item = get_object_or_404(Item, pk=kwargs['pk'])
        session = stripe_service.create_session(item)
        return Response({'session_id': session.id}, status=status.HTTP_200_OK)

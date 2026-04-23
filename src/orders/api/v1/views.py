from django.conf import settings
from django.shortcuts import get_object_or_404
from django.urls import reverse
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView, Response

from orders.api.v1.serializers import ItemSerializer, OrderSerializer
from orders.models import Item, Order
from orders.services import stripe_service


class ItemHTMLView(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    renderer_classes = (TemplateHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        item = self.get_object()
        serializer = self.get_serializer(item)
        return Response(
            {
                'item': serializer.data,
                'public_key': settings.STRIPE_PUBLIC_KEY,
            },
            template_name='item_detail.html',
        )


class ItemBuyView(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        item: Item = get_object_or_404(Item, pk=pk)
        item_url: str = reverse('item', kwargs={'pk': pk})
        session = stripe_service.create_session(
            item=item, success_url=item_url, cancel_url=item_url
        )
        return Response({'session_id': session.id}, status=status.HTTP_200_OK)


class OrderHTMLView(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    renderer_classes = (TemplateHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        order: Order = self.get_object()
        serializer = self.get_serializer(order)
        return Response(
            {
                'order': serializer.data,
                'public_key': settings.STRIPE_PUBLIC_KEY,
            },
            template_name='order.html',
        )


class OrderBuyView(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        order = get_object_or_404(Order, pk=pk)
        if order.is_paid:
            return Response(
                {'error': 'Order is already paid'}, status=status.HTTP_400_BAD_REQUEST
            )
        item_url = reverse('order', kwargs={'pk': pk})
        session = stripe_service.create_session(
            order=order, success_url=item_url, cancel_url=item_url
        )
        return Response({'session_id': session.id}, status=status.HTTP_200_OK)

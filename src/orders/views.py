# from rest_framework.viewsets import ModelViewSet, APIViewSet
from django.views.generic import DetailView

from orders.models import Item


class ItemView(DetailView):
    model = Item
    template_name = 'item.html'

from rest_framework.serializers import ModelSerializer

from orders.models import Item, Order


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
        read_only_fields = ('id',)


class OrderSerializer(ModelSerializer):
    items = ItemSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at', 'total', 'currency')

from rest_framework.serializers import ModelSerializer

from orders.models import Item, ItemInOrder, Order


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
        read_only_fields = ('id',)


class ItemInOrderSerializer(ModelSerializer):
    item = ItemSerializer()

    class Meta:
        model = ItemInOrder
        fields = ('id', 'item', 'quantity')


class OrderSerializer(ModelSerializer):
    iteminorder_set = ItemInOrderSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'iteminorder_set', 'total', 'currency')
        read_only_fields = ('id', 'total', 'currency')

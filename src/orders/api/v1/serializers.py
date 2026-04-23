from rest_framework.serializers import ModelSerializer

from orders.models import Item, ItemInOrder, Order


class ItemSerializer(ModelSerializer):
    """Сериализатор для модели Item."""

    class Meta:
        model = Item
        fields = '__all__'
        read_only_fields = ('id',)


class ItemInOrderSerializer(ModelSerializer):
    """Сериализатор для модели ItemInOrder."""

    item = ItemSerializer()

    class Meta:
        model = ItemInOrder
        fields = ('id', 'item', 'quantity')


class OrderSerializer(ModelSerializer):
    """Сериализатор для модели Order."""

    iteminorder_set = ItemInOrderSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'iteminorder_set', 'total', 'currency', 'is_paid')
        read_only_fields = ('id', 'total', 'currency')

from django.contrib import admin

from orders.models import Discount, Item, Order, Tax


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'currency')
    search_fields = ('name',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'updated_at', 'is_paid', 'total', 'currency')
    search_fields = ('id',)


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'value', 'currency')
    search_fields = ('id', 'name')


@admin.register(Tax)
class TaxAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'value', 'currency')
    search_fields = (
        'id',
        'name',
    )

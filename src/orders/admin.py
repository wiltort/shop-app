from django import forms
from django.contrib import admin
from django.core.exceptions import ValidationError

from orders.models import Discount, Item, ItemInOrder, Order, Tax


class ItemInOrderInline(admin.TabularInline):
    model = ItemInOrder
    extra = 1
    min_num = 1


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'currency')
    search_fields = ('name',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'updated_at', 'is_paid', 'total', 'currency')
    search_fields = ('id',)
    inlines = (ItemInOrderInline,)
    form = OrderForm

    def save_related(self, request, form, formsets, change):
        """
        После сохранения заказа проверяем валюту товаров и устанавливаем валюту заказа.
        """
        super().save_related(request, form, formsets, change)
        order = form.instance
        # Получаем все товары в заказе через промежуточную модель
        items_in_order = order.iteminorder_set.all()
        if items_in_order:
            currencies = {
                item_in_order.item.currency for item_in_order in items_in_order
            }
            if len(currencies) > 1:
                raise ValidationError(
                    'Все товары в заказе должны иметь одинаковую валюту.'  # noqa
                )
            # Устанавливаем валюту заказа на основе валюты первого товара
            order.currency = items_in_order[0].item.currency
            order.save(update_fields=['currency'])


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

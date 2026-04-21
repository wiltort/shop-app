from django.conf import settings
from django.db import models


# Create your models here.
class Item(models.Model):
    """Модель для товара."""

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    name = models.CharField(max_length=255, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    currency = models.CharField(
        max_length=3,
        verbose_name='Валюта',
        choices=settings.CURRENCIES,
        default=settings.DEFAULT_CURRENCY,
    )


class ItemInOrder(models.Model):
    """Модель для товара в заказе."""

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'

    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name='Товар')
    order = models.ForeignKey('Order', on_delete=models.CASCADE, verbose_name='Заказ')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')


class Order(models.Model):
    """Модель для заказа."""

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ('-created_at',)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлен')
    items = models.ManyToManyField(Item, verbose_name='Товары', through=ItemInOrder)
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Итого')
    currency = models.CharField(
        max_length=3,
        verbose_name='Валюта',
        choices=settings.CURRENCIES,
        default=settings.DEFAULT_CURRENCY,
    )
    is_paid = models.BooleanField(default=False, verbose_name='Оплачен')


class Discount(models.Model):
    """Модель для скидки."""

    class Meta:
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'

    name = models.CharField(max_length=255, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    value = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Значение'
    )
    currency = models.CharField(
        max_length=3,
        verbose_name='Валюта',
        choices=settings.CURRENCIES,
        default=settings.DEFAULT_CURRENCY,
    )


class Tax(models.Model):
    """Модель для налога."""

    class Meta:
        verbose_name = 'Налог'
        verbose_name_plural = 'Налоги'

    name = models.CharField(max_length=255, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    value = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Значение'
    )
    currency = models.CharField(
        max_length=3,
        verbose_name='Валюта',
        choices=settings.CURRENCIES,
        default=settings.DEFAULT_CURRENCY,
    )

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


class Order(models.Model):
    """Модель для заказа."""

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ('-created_at',)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлен')
    items = models.ManyToManyField(Item, verbose_name='Товары')

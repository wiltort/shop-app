from django.urls import path

from orders.api.v1.views import ItemBuyView, ItemHTMLView

urlpatterns = [
    path('items/<int:pk>/', ItemHTMLView.as_view(), name='item'),
    path('buy/<int:pk>/', ItemBuyView.as_view(), name='item-buy'),
]

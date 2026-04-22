from django.urls import include, path

from orders.views import ItemView

urlpatterns = [
    path('api/', include('orders.api.urls')),
    path('items/<int:pk>/', ItemView.as_view(), name='item-detail'),
]

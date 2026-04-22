from django.urls import include, path

urlpatterns = [path('v1/', include('orders.api.v1.urls'))]

from rest_framework.viewsets import ModelViewSet
from .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer

class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

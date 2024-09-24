import africastalking
from django.conf import settings
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer

# Initialize Africa's Talking SMS service with your credentials
africastalking.initialize(username=settings.USERNAME, api_key=settings.API_KEY)
sms = africastalking.SMS

def send_sms(to, message):
    
    try:
        # Send SMS through Africa's Talking API
        response = sms.send(message, [to])
        print(f"SMS sent successfully: {response}")
    except Exception as e:
        print(f"Failed to send SMS: {e}")
       


class CustomerViewSet(viewsets.ModelViewSet):
    
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]


class OrderViewSet(viewsets.ModelViewSet):
   
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        
        order = serializer.save()
        customer = order.customer

        # Prepare the SMS content
        message = f"Hello {customer.name}, your order for '{order.item}' worth {order.amount} has been placed successfully!"

        # Send the SMS to the customer's phone number
        send_sms(customer.phone_number, message)

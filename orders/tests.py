from django.test import TestCase
from .models import Customer, Order

class CustomerModelTest(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(name="John Doe", code="JD123")

    def test_customer_creation(self):
        self.assertEqual(self.customer.name, "John Doe")

class OrderModelTest(TestCase):
    def setUp(self):
        customer = Customer.objects.create(name="John Doe", code="JD123")
        self.order = Order.objects.create(customer=customer, item="Laptop", amount=1000)

    def test_order_creation(self):
        self.assertEqual(self.order.item, "Laptop")

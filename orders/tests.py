from django.test import TestCase
from .models import Customer, Order

class CustomerModelTest(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(name="Mike Ngige", code="MN123")

    def test_customer_creation(self):
        self.assertEqual(self.customer.name, "Mike Ngige")

class OrderModelTest(TestCase):
    def setUp(self):
        customer = Customer.objects.create(name="Mike Ngige" code="MN123")
        self.order = Order.objects.create(customer=customer, item="Laptop", amount=1000)

    def test_order_creation(self):
        self.assertEqual(self.order.item, "Laptop")

from django.test import TestCase
from customers.models import Customer

class CustomerModelTest(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(
            first_name="John",
            last_name="Doe",
            email="john@example.com"
        )

    def test_customer_creation(self):
        """Test if a customer object is created successfully"""
        self.assertEqual(self.customer.first_name, "John")
        self.assertEqual(self.customer.last_name, "Doe")
        self.assertEqual(self.customer.email, "john@example.com")

    def test_str_representation(self):
        """Test the __str__ method"""
        self.assertEqual(str(self.customer), "John Doe")

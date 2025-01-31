from django.test import TestCase, Client
from customers.models import Customer
from django.urls import reverse

class CustomerViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.customer = Customer.objects.create(
            first_name="Jane",
            last_name="Smith",
            email="jane@example.com"
        )

    def test_customer_list_view(self):
        """Test GET request to retrieve customers"""
        response = self.client.get(reverse('customer-list'))  # Ensure you have a URL named 'customer-list'
        self.assertEqual(response.status_code, 200)

    def test_customer_detail_view(self):
        """Test retrieving a single customer"""
        response = self.client.get(reverse('customer-detail', args=[self.customer.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Jane")

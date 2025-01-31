from django.test import TestCase
from customers.tests import CustomerForm

class CustomerFormTest(TestCase):
    def test_valid_form(self):
        """Test a valid customer form"""
        form_data = {'first_name': 'Alice', 'last_name': 'Brown', 'email': 'alice@example.com'}
        form = CustomerForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        """Test an invalid customer form (missing email)"""
        form_data = {'first_name': 'Alice', 'last_name': 'Brown'}
        form = CustomerForm(data=form_data)
        self.assertFalse(form.is_valid())

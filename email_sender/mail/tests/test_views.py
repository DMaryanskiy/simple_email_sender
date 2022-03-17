from django import forms
from django.test import TestCase, Client
from django.urls import reverse


class MainPageTests(TestCase):
    """ class with tests for index view function """
    def setUp(self):
        """ setting up common conditions for all tests """
        self.guest_client = Client()
    
    def test_pages_use_correct_template(self):
        """ testing if pages use correct template """
        response = self.guest_client.get(reverse('mail:index'))
        self.assertTemplateUsed(response, 'index.html')
    
    def test_pages_show_correct_context(self):
        """ checking for correct context """
        response = self.guest_client.get(reverse('mail:index'))
        form_fields = {
            'subject': forms.fields.CharField,
            'recipents': forms.fields.CharField,
            'message': forms.fields.CharField,
        }

        for value, expected in form_fields.items():
            with self.subTest(value=value):
                form_field = response.context.get('form').fields.get(value)
                self.assertIsInstance(form_field, expected)

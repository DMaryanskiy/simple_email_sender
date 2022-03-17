from django.test import TestCase, Client


class StaticURLTests(TestCase):
    """ URL tests """
    def setUp(self):
        """ setting up common conditions for all tests """
        self.guest_client = Client()

    def test_mainpage(self):
        """ checking if main page opens correctly """
        response = self.guest_client.get('/')
        self.assertEqual(response.status_code, 200)

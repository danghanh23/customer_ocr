from django.test import TestCase, SimpleTestCase

# Create your tests here.
class SimpleTests(SimpleTestCase):
    def test_home_page_sattus(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
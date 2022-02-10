from django.test import TestCase

# Create your tests here.

class SimpleTests(TestCase):
    def test_homepage_status_code(self):
        response = self.client.get('/hello/')
        self.assertEqual(response.status_code, 200)
    
    def test_aboutpage_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
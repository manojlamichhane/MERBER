from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.

class test_views (TestCase):
    def test_web_index(self):
        client = Client()
        response = client.get(reverse('web_index'))
        self.assertEqual(response.status_code,200)
    
    def test_web_login(self):
        client = Client()
        response = client.get(reverse('web_orderhome_login'))
        self.assertEqual(response.status_code,200)    
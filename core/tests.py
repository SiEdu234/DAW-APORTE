from django.test import TestCase
from django.urls import reverse

class AboutViewTest(TestCase):
    def test_about_view_status_code(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_about_view_content(self):
        response = self.client.get(reverse('about'))
        self.assertContains(response, "<h1>Prueba Django</h1>")
        self.assertContains(response, "1. Soy Rafael Vera Garcia")
        self.assertContains(response, "14. Soy Rafael Vera Garcia")

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status


class shortenerAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_short_url(self):
        url = reverse('shortener')
        response = self.client.post(
            url, data={'original_url': 'https://docs.python.org/3/reference/datamodel.html'}, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        return response.data

    def test_create_short_url_already_exist(self):
        first_url = self.test_create_short_url()
        url = reverse('shortener')
        response = self.client.post(
            url, data={'original_url': first_url['original_url']}, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_redirect_to_long_url(self):
        first_url = self.test_create_short_url()
        url = reverse('redirect-original-url', kwargs={'short_url': first_url['short_url']})
        response = self.client.get(
            url, data={'original_url': first_url['original_url']}, format="json")
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

from django.test import TestCase
from api.models import Endpoint
from django.utils import timezone
from django.urls import reverse
# Create your tests here.


# Models test
class EndpointModelTest(TestCase):

    def test_endpoint_creation_url(self):
        endpoint = Endpoint(
            url='abc', verb='GET', response_code='200',
            content_type='json', encoding='utf-8',
            body="yes, this is only a test")
        self.assertEqual(str(endpoint), endpoint.url)

    def test_endpoint_creation_verb(self):
        endpoint = Endpoint(
            url='abc', verb='GET', response_code='200',
            content_type='json', encoding='utf-8',
            body="yes, this is only a test")
        self.assertEqual(str(endpoint), endpoint.url)

    def test_endpoint_creation_response_code(self):
        endpoint = Endpoint(
            url='abc', verb='GET', response_code='200',
            content_type='json', encoding='utf-8',
            body="yes, this is only a test")
        self.assertEqual(str(endpoint), endpoint.url)

    def test_endpoint_creation_content_type(self):
        endpoint = Endpoint(
            url='abc', verb='GET', response_code='200',
            content_type='json', encoding='utf-8',
            body="yes, this is only a test")
        self.assertEqual(str(endpoint), endpoint.url)

    def test_endpoint_creation_encoding(self):
        endpoint = Endpoint(
            url='abc', verb='GET', response_code='200',
            content_type='json', encoding='utf-8',
            body="yes, this is only a test")
        self.assertEqual(str(endpoint), endpoint.url)

    def test_endpoint_creation_body(self):
        endpoint = Endpoint(
            url='abc', verb='GET', response_code='200',
            content_type='json', encoding='utf-8',
            body="yes, this is only a test")
        self.assertEqual(str(endpoint), endpoint.url)


# View test
class WelcomeViewTest(TestCase):

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


class ListViewTest(TestCase):

    def test_one_entry(self):
        Endpoint.objects.create(
            url='abc', verb='GET', response_code='200',
            content_type='json', encoding='utf-8',
            body="yes, this is only a test")
        response = self.client.get('/endpoint/list')
        self.assertContains(response, 'abc')
        self.assertContains(response, 'GET')

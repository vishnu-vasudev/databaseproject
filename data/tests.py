from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse


class Sample(TestCase):
    def setUp(self):
        selfself.client = APIClient
    
    def test_sample(self):
        url = reverse('test')
        print(url)
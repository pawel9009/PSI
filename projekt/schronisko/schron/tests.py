from rest_framework.test import APITestCase
from . import views
from .models import Pracownicy
from .models import Klient
from rest_framework import status
from rest_framework.reverse import reverse
from django.utils.http import urlencode
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django import urls

class KlientTests(APITestCase):

    def post_klient(self, tel):
        url = reverse(views.Klientt.name)
        data = {'tel': tel}
        response = self.client.post(url, data, format('json'))
        return response

    def test_post_and_get_klient(self):
        nowe_tel = 777
        response = self.post_klient(nowe_tel)
        assert response.status_code == status.HTTP_201_CREATED
        assert Klient.objects.count() == 1
        assert Klient.objects.get().tel == nowe_tel

    def test_post_existing_klient(self):
        url = reverse(views.Klientt.name)
        new_tel = 777
        data = {'tel': new_tel}
        response_one = self.post_klient(new_tel)
        assert response_one.status_code == status.HTTP_201_CREATED
        response_two = self.post_klient(new_tel)
        print(response_two)
        assert response_two.status_code == status.HTTP_400_BAD_REQUEST




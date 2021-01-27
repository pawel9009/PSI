from rest_framework.test import APITestCase
from . import views
from .models import Klient
from .models import Zwiarzak
from rest_framework import status
from rest_framework.reverse import reverse
from django.utils.http import urlencode


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


class ZwierzakTests(APITestCase):

    def post_zwierzak(self, imie):
        url = reverse(views.zwierzak.name)
        data = {'imie': imie}
        response = self.client.post(url, data, format('json'))
        return response

    def test_post_and_get_zwierzak(self):
        nowe_imie = "rex"
        response = self.post_zwierzak(nowe_imie)
        assert response.status_code == status.HTTP_201_CREATED
        assert Zwiarzak.objects.count() == 1
        assert Zwiarzak.objects.get().imie == nowe_imie

    def test_filter_zwierzak_by_gatunek(self):
        zwierzak_gatunek_one = 'pies'
        zwierzak_gatunek_two = 'kot'
        self.post_zwierzak(zwierzak_gatunek_one)
        self.post_zwierzak(zwierzak_gatunek_two)
        filter_by_gatunek = {'gatunek': zwierzak_gatunek_one}
        url = '{0}?{1}'.format(reverse(views.zwierzak.name), urlencode(filter_by_gatunek))
        print(url)
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        assert response.data['results'][0]['name'] == zwierzak_gatunek_one


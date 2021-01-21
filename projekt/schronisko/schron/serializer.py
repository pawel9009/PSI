from rest_framework import serializers
from .models import Zwiarzak
from .models import Pracownicy
from .models import Adopcja
from .models import Klient
from rest_framework.serializers import HyperlinkedIdentityField
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class ZwierzakSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zwiarzak
        fields = ['url', 'id', 'imie', 'gatunek', 'rasa', 'wiek', 'waga']


class PracownicySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pracownicy
        fields = ['url', 'id', 'imie', 'nazwisko', 'stanowisko', 'tel', 'adres']


class KlientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Klient
        fields = ['url', 'id', 'imie', 'nazwisko', 'tel']


class AdopcjaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adopcja
        fields = ['url', 'id', 'data', 'idklienta', 'idzwierz']

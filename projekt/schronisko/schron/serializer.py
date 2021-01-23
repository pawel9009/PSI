from rest_framework import serializers
from .models import Zwiarzak
from .models import Pracownicy
from .models import Adopcja
from .models import Klient
from rest_framework.serializers import HyperlinkedIdentityField
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class ZwierzakSerializer(serializers.ModelSerializer):
    zwierze = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='adopcja-detail')

    class Meta:
        model = Zwiarzak
        fields = ['url', 'id', 'imie', 'gatunek', 'rasa', 'wiek', 'waga', 'zwierze']


class PracownicySerializer(serializers.ModelSerializer):
    wlasciciel = serializers.ReadOnlyField(source='wlasciciel.username')
    class Meta:
        model = Pracownicy
        fields = ['url', 'id', 'imie', 'nazwisko', 'stanowisko', 'tel', 'adres', 'wlasciciel']


class KlientSerializer(serializers.HyperlinkedModelSerializer):
    klient = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='adopcja-detail')
    class Meta:
        model = Klient
        fields = ['url', 'id', 'imie', 'nazwisko', 'tel', 'klient']


class AdopcjaSerializer(serializers.HyperlinkedModelSerializer):
    idklienta = serializers.SlugRelatedField(queryset=Klient.objects.all(), slug_field='imie')
    idzwierz = serializers.SlugRelatedField(queryset=Zwiarzak.objects.all(), slug_field='imie')
    class Meta:
        model = Adopcja
        fields = ['url', 'id', 'data', 'idklienta','idzwierz' ]


class UserPracownikSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pracownicy
        fields = ['url', 'imie', 'nazwisko']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    pracownicy = UserPracownikSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['url', 'pk', 'username', 'pracownicy']
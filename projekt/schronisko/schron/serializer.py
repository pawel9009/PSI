from rest_framework import serializers
from .models import Zwiarzak
from .models import Pracownicy
from .models import Adopcja
from .models import Klient
from django.core.validators import RegexValidator
litery = RegexValidator(r'^[a-zA-Z]*$', 'Only litery characters are allowed.')




class ZwierzakSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zwiarzak
        fields = ['id', 'imie','gatunek', 'rasa', 'wiek', 'waga']



class PracownicySerializer(serializers.ModelSerializer):
     class Meta:
         model = Pracownicy
         fields = ['id', 'imie','nazwisko', 'stanowisko', 'tel', 'adres']




class KlientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Klient
        fields = ['id', 'imie','nazwisko', 'tel']



class AdopcjaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adopcja
        fields = ['id', 'data','idklienta', 'idzwierz']


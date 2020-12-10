from rest_framework import serializers
from .models import Zwiarzak
from .models import Pracownicy
from .models import Adopcja
from .models import Klient
from django.core.validators import RegexValidator
litery = RegexValidator(r'^[a-zA-Z]*$', 'Only litery characters are allowed.')


class ZwierzakSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    imie = serializers.CharField(max_length=20, required=True, validators=[litery])
    gatunek = serializers.CharField(required=True, max_length=30)
    rasa = serializers.CharField(max_length=30 , required=True)
    wiek = serializers.DecimalField(required=True, max_digits=2, decimal_places=0)
    waga = serializers.DecimalField(required=True, max_digits=2, decimal_places=0)

    def create(self, validated_data):
        return Zwiarzak.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.imie = validated_data.get('imie', instance.imie)
        instance.gatunek = validated_data.get('gatunek', instance.gatunek)
        instance.rasa = validated_data.get('rasa', instance.rasa)
        instance.wiek = validated_data.get('wiek', instance.wiek)
        instance.waga = validated_data.get('waga', instance.waga)
        instance.save()
        return instance

# class ZwierzakSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Zwiarzak
#         fields = ['id', 'imie','gatunek', 'rasa', 'wiek', 'waga']

class PracownicySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    imie = serializers.CharField(max_length=20, required=True, validators=[litery])
    nazwisko = serializers.CharField(max_length=20, required=True, validators=[litery])
    stanowisko = serializers.CharField(max_length=20, required=True, validators=[litery])
    tel = serializers.DecimalField(required=True, max_digits=11, decimal_places=0)
    adres = serializers.CharField(max_length=20, required=True,)

    def create(self, validated_data):
        return Pracownicy.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.imie = validated_data.get('imie', instance.imie)
        instance.nazwisko = validated_data.get('nazwisko', instance.nazwisko)
        instance.stanowisko = validated_data.get('stanowisko', instance.stanowisko)
        instance.tel = validated_data.get('tel', instance.tel)
        instance.adres = validated_data.get('adres', instance.adres)
        instance.save()
        return instance

#class PracownikSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Pracownicy
#         fields = ['id', 'imie','nazwisko', 'stanowisko', 'tel', 'adres']

class KlientSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    imie = serializers.CharField(max_length=20, required=True, validators=[litery])
    nazwisko = serializers.CharField(max_length=20, required=True, validators=[litery])
    tel = serializers.DecimalField(required=True, max_digits=11, decimal_places=0)

    def create(self, validated_data):
        return Klient.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.imie = validated_data.get('imie', instance.imie)
        instance.nazwisko = validated_data.get('nazwisko', instance.nazwisko)
        instance.tel = validated_data.get('tel', instance.tel)
        instance.save()
        return instance


# class KlientSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Klient
#         fields = ['id', 'imie','nazwisko', 'tel']


class AdopcjaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    data = serializers.DateField(required=True)
    idklienta = serializers.IntegerField()
    idzwierz = serializers.IntegerField()

    def create(self, validated_data):
        return Adopcja.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.data = validated_data.get('data', instance.data)
        instance.idklienta = validated_data.get('idklienta', instance.idklienta)
        instance.idzwierz = validated_data.get('idzwierz', instance.idzwierz)

        instance.save()
        return instance

# class AdopcjaSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Adopcja
#         fields = ['id', 'data','idklienta', 'idzwierz']


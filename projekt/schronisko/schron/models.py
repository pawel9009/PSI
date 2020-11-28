from django.db import models


class Zwiarzak(models.Model):
    id = models.AutoField(primary_key=True)
    imie = models.CharField(max_length=30, default="")
    gatunek = models.CharField(max_length=30, default="")
    rasa = models.CharField(max_length=30, default="")
    wiek = models.DecimalField(max_digits=4, decimal_places=2 , default=0)
    waga = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    def __str__(self):
        return self.imie


class Pracownicy(models.Model):
    id = models.AutoField(primary_key=True)
    imie = models.CharField(max_length=30, default="")
    nazwisko = models.CharField(max_length=30, default="")
    stanowisko = models.CharField(max_length=30, default="")
    tel = models.DecimalField(max_digits=11, decimal_places=0 , default=0)
    adres = models.CharField(max_length=30, default="")
    def __str__(self):
        return self.imie + ' ' + self.nazwisko


class Klient(models.Model):
    id = models.AutoField(primary_key=True)
    imie = models.CharField(max_length=30, default="")
    nazwisko = models.CharField(max_length=30, default="")
    tel = models.DecimalField(max_digits=11, decimal_places=0 , default=0)

    def __str__(self):
        return self.imie + ' ' + self.nazwisko


class Adopcja(models.Model):
    id = models.AutoField(primary_key=True)
    data = models.DateField()
    idklienta = models.ForeignKey(Klient, on_delete=models.SET_NULL, null=True)
    idzwierz = models.ForeignKey(Zwiarzak, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.data)



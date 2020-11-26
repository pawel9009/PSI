from django.db import models

class Zwiarzak(models.Model):
    idzwierzak = models.AutoField(primary_key=True)
    imie = models.CharField(max_length=30, default="tak")
    gatunek = models.CharField(max_length=30, default="pies")
    rasa = models.CharField(max_length=30, default="cos")
    wiek = models.DecimalField(max_digits=30, decimal_places=2 , default=0)
    masa = models.DecimalField(max_digits=30, decimal_places=2, default=3)
    def __str__(self):
        return self.imie

class Pracownicy(models.Model):
    idpracownika = models.AutoField(primary_key=True)
    imie = models.CharField(max_length=30, default="")
    nazwisko = models.CharField(max_length=30, default="")
    stanowisko = models.CharField(max_length=30, default="cos")
    tel = models.DecimalField(max_digits=11, decimal_places=0 , default=0)
    adres = models.CharField(max_length=30, default="cos")
    def __str__(self):
        return self.imie

class Klient(models.Model):
    idpklienta = models.AutoField(primary_key=True)
    imie = models.CharField(max_length=30, default="")
    nazwisko = models.CharField(max_length=30, default="")
    tel = models.DecimalField(max_digits=11, decimal_places=0 , default=0)
    def __str__(self):
        return self.imie

class Adopcja(models.Model):
    idadopcji = models.AutoField(primary_key=True)
    data = models.DateField()
    idklient = models.ForeignKey(Klient,on_delete=models.CASCADE,null=True)
    idzwierzak = models.ForeignKey(Zwiarzak,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.data


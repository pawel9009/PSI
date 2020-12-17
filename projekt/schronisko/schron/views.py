from rest_framework import generics, permissions, authentication
from rest_framework.views import APIView
from rest_framework.reverse import reverse
from rest_framework.response import Response
from .models import Pracownicy, Klient as klientt, Zwiarzak, Adopcja
from .serializer import PracownicySerializer, KlientSerializer, ZwierzakSerializer,AdopcjaSerializer
from django.contrib.auth.models import User


class Pracownik(generics.ListCreateAPIView):
    queryset = Pracownicy.objects.all()
    serializer_class = PracownicySerializer
    name = "Pracownik"
    permission_classes = [permissions.IsAuthenticated] # bez tego nei chce dodawać


class PracownikDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pracownicy.objects.all()
    serializer_class = PracownicySerializer
    permission_classes = [permissions.IsAdminUser]  #tylko admin i ci co maja prawa moga usuwac


class PracownikDodaj(generics.ListCreateAPIView):
    queryset = Pracownicy.objects.all()
    serializer_class = PracownicySerializer
    name = 'Pracownik-list'
    search_fields = ['imie', 'stanowsko']
    ordering_fields = ['imie', 'nazwisko', 'stanowisko']
    permission_classes = [permissions.IsAdminUser]#dostepne dla zalogowanych

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

#----------------------------------------------------------


class Klient(generics.ListCreateAPIView):
    queryset = klientt.objects.all()
    serializer_class = KlientSerializer
    name = "Pracownik"
    permission_classes = [permissions.IsAuthenticated] # bez tego nei chce dodawać


class KlientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = klientt.objects.all()
    serializer_class = KlientSerializer
    permission_classes = [permissions.IsAdminUser]


class KlientDodaj(generics.ListCreateAPIView):
    queryset = klientt.objects.all()
    serializer_class = KlientSerializer
    name = 'Klient-list'
    search_fields = ['imie', 'stanowsko']
    ordering_fields = ['imie', 'nazwisko', 'stanowisko']
    permission_classes = [permissions.IsAdminUser]#dostepne dla zalogowanych

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


#---------------------------------------------------

class zwierzak(generics.ListCreateAPIView):
    queryset = Zwiarzak.objects.all()
    serializer_class = ZwierzakSerializer
    name = "zwierzak"
    permission_classes = [permissions.IsAuthenticated]


class zwierzakDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Zwiarzak.objects.all()
    serializer_class = ZwierzakSerializer
    permission_classes = [permissions.IsAdminUser]

class zwierzakdodaj(generics.ListCreateAPIView):
    queryset = Zwiarzak.objects.all()
    serializer_class = ZwierzakSerializer
    name = 'zwierzak-list'
    search_fields = ['imie', 'stanowsko']
    ordering_fields = ['imie', 'nazwisko', 'stanowisko']
    permission_classes = [permissions.IsAdminUser]#dostepne dla zalogowanych

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

#-------------------------------------------------------

class adopcja(generics.ListCreateAPIView):
    queryset = Adopcja.objects.all()
    serializer_class = AdopcjaSerializer
    name = "adopcja"
    permission_classes = [permissions.IsAuthenticated]


class adopcjadetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Adopcja.objects.all()
    serializer_class = AdopcjaSerializer
    permission_classes = [permissions.IsAdminUser]




class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({'pracownik': reverse(Pracownik.name, request=request),
                         'zwierzak': reverse(zwierzak.name, request=request),
                         'klient': reverse(klientt.name, request=request),

                         })
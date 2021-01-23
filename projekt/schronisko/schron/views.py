from rest_framework import generics, permissions, authentication
from rest_framework.views import APIView
from rest_framework.reverse import reverse
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Pracownicy, Klient, Zwiarzak, Adopcja
from .serializer import PracownicySerializer, KlientSerializer, ZwierzakSerializer,AdopcjaSerializer,UserSerializer


class Pracownik(generics.ListCreateAPIView):
    queryset = Pracownicy.objects.all()
    serializer_class = PracownicySerializer
    name = "Pracownik"
    filterset_fields = ['imie', 'nazwisko', 'stanowisko']
    search_fields = ['imie', 'nazwisko', 'stanowisko']
    ordering_fields = ['imie', 'nazwisko', 'stanowisko']
    permission_classes = [permissions.IsAuthenticated] # bez tego nei chce dodawać

    def perform_create(self, serializer):
        serializer.save(wlasciciel=self.request.user)


class PracownikDetail(generics.RetrieveUpdateDestroyAPIView):
    name = 'pracownicy-detail'
    queryset = Pracownicy.objects.all()
    serializer_class = PracownicySerializer
    permission_classes = [permissions.IsAdminUser]  #tylko admin i ci co maja prawa moga usuwac


class PracownikDodaj(generics.ListCreateAPIView):
    queryset = Pracownicy.objects.all()
    serializer_class = PracownicySerializer
    name = 'Pracownik-list'
    permission_classes = [permissions.IsAdminUser]#dostepne dla zalogowanych

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

#----------------------------------------------------------


class Klientt(generics.ListCreateAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer
    name = "Klient"
    filterset_fields = ['imie', 'nazwisko']
    search_fields = ['imie', 'nazwisko']
    ordering_fields = ['imie', 'nazwisko']
    permission_classes = [permissions.IsAuthenticated] # bez tego nei chce dodawać


class KlientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer
    name = 'klient-detail'
    permission_classes = [permissions.IsAdminUser]


class KlientDodaj(generics.ListCreateAPIView):
    queryset = Klient.objects.all()
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
    filterset_fields = ['imie', 'gatunek', 'rasa', 'waga', 'wiek']
    search_fields = ['imie', 'gatunek', 'rasa', 'waga', 'wiek']
    ordering_fields = ['imie', 'gatunek', 'rasa', 'waga', 'wiek']
    permission_classes = [permissions.IsAuthenticated]


class ZwierzakDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Zwiarzak.objects.all()
    name = "zwiarzak-detail"
    serializer_class = ZwierzakSerializer
    permission_classes = [permissions.IsAdminUser]

class zwierzakdodaj(generics.ListCreateAPIView):
    queryset = Zwiarzak.objects.all()
    serializer_class = ZwierzakSerializer
    name = 'zwierzak-list'
    permission_classes = [permissions.IsAdminUser] #dostepne dla zalogowanych

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

#-------------------------------------------------------


class adopcja(generics.ListCreateAPIView):
    queryset = Adopcja.objects.all()
    serializer_class = AdopcjaSerializer
    name = "adopcja"
    ordering_fields = ['data']
    permission_classes = [permissions.IsAuthenticated]


class adopcjadetail(generics.RetrieveUpdateDestroyAPIView):
    name = 'adopcja-detail'
    queryset = Adopcja.objects.all()
    serializer_class = AdopcjaSerializer
    permission_classes = [permissions.IsAdminUser]


class adopcjadodaj(generics.ListCreateAPIView):
    queryset = Adopcja.objects.all()
    serializer_class = AdopcjaSerializer
    name = 'adopcja-list'
    search_fields = ['imie', 'stanowsko']
    ordering_fields = ['imie', 'nazwisko', 'stanowisko']
    permission_classes = [permissions.IsAdminUser]#dostepne dla zalogowanych

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name='user-list'

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name='user-detail'



class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({'pracownik': reverse(Pracownik.name, request=request),
                         'zwierzak': reverse(zwierzak.name, request=request),
                         'klient': reverse(Klientt.name, request=request),
                         'adopcja': reverse(adopcja.name, request=request),
                         'uzytkowicy': reverse(UserList.name, request=request),
                         }
                        )

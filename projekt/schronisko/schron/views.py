from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.response import Response
from .models import Pracownicy, Klient, Zwiarzak
from .serializer import PracownicySerializer, KlientSerializer, ZwierzakSerializer
from rest_framework import permissions
from django.contrib.auth.models import User


class PracownikinfoList(generics.ListCreateAPIView):
    queryset = Pracownicy.objects.all()
    serializer_class = PracownicySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    name = 'Pracownicyinfo-list'
    search_fields = ['name']
    ordering_fields = ['name']


class PracownicyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pracownicy.objects.all()
    serializer_class = PracownicySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    name = 'Pracownicy-detail'


class PracownikList(generics.ListCreateAPIView):
    queryset = Pracownicy.objects.all()
    serializer_class = PracownicySerializer
    name = 'Pracownik-list'
    search_fields = ['imie', 'stanowsko']
    ordering_fields = ['imie', 'nazwisko', 'stanowisko']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PracownikDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pracownicy.objects.all()
    serializer_class = PracownicySerializer
    name = 'Pracownik-detail'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


#--------------------------------------------------------------------------


class KlientinfoList(generics.ListCreateAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer
    name = 'Klienciinfo-list'
    search_fields = ['name']
    ordering_fields = ['name']


class KlienciDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer
    name = 'Klienci-detail'


class KlienciList(generics.ListCreateAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer
    name = 'Klienci-list'
    search_fields = ['imie', 'stanowsko', 'tel']
    ordering_fields = ['imie', 'nazwisko', 'tel']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class KlientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer
    name = 'Klient-detail'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#--------------------------------------------------------------------


class ZwierzakinfoList(generics.ListCreateAPIView):
    queryset = Zwiarzak.objects.all()
    serializer_class = ZwierzakSerializer
    name = 'Zwiarzakinfo-list'
    search_fields = ['name']
    ordering_fields = ['name']


class ZwierzakiDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Zwiarzak.objects.all()
    serializer_class = ZwierzakSerializer
    name = 'Zwiarzak-detail'


class ZwierzakList(generics.ListCreateAPIView):
    queryset = Zwiarzak.objects.all()
    serializer_class = ZwierzakSerializer
    name = 'Zwiarzak-list'
    search_fields = ['imie', 'stanowsko', 'tel']
    ordering_fields = ['imie', 'nazwisko', 'tel']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ZwierzakDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Zwiarzak.objects.all()
    serializer_class = ZwierzakSerializer
    name = 'Zwiarzak-detail'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({'Pracownicy': reverse(PracownikList.name, request=request),
                         'Klienci': reverse(KlienciList.name, request=request),
                         'Zwierzaki': reverse(ZwierzakList.name, request=request),
                         })

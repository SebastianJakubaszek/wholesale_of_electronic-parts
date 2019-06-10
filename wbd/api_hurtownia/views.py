from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import viewsets
from .models import *
from .api import serializers
import django_filters



class HurtownieViewsApi(viewsets.ModelViewSet):
    queryset = Hurtownie.objects.all()
    serializer_class = serializers.HurtownieSerializer


class KontoViewsApi(viewsets.ModelViewSet):
    queryset = Konto.objects.all()
    serializer_class = serializers.KontoSerializer


class KlientViewsApi(viewsets.ModelViewSet):
    serializer_class = serializers.KlientSerializer
    queryset = Klient.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        imie = self.request.query_params.get('imie', None)
        nazwisko = self.request.query_params.get('nazwisko',None)
        if imie is not None:
            print('wszedlem1')
            queryset = queryset.filter(imie__icontains=imie)
        if nazwisko is not None:
            print('wszedlem2')
            queryset = queryset.filter(nazwisko__icontains=nazwisko)
        return queryset

class StanowiskaViewsApi(viewsets.ModelViewSet):
    queryset = Stanowiska.objects.all()
    serializer_class = serializers.StanowiskaSerializer


class WynagrodzenieViewsApi(viewsets.ModelViewSet):
    queryset = Wynagrodzenie.objects.all()
    serializer_class = serializers.WynagrodzenieSerializer


class PracownikViewsApi(viewsets.ModelViewSet):
    queryset = Pracownik.objects.all()
    serializer_class = serializers.PracownikSerializer


class MagazynViewsApi(viewsets.ModelViewSet):
    queryset = Magazyn.objects.all()
    serializer_class = serializers.MagazynSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('nazwa', )

class DostawcaViewsApi(viewsets.ModelViewSet):
    queryset = Dostawca.objects.all()
    serializer_class = serializers.DostawcaSerializer


class DzialViewsApi(viewsets.ModelViewSet):
    queryset = Dzial.objects.all()
    serializer_class = serializers.DzialSerializer


class ProducentViewsApi(viewsets.ModelViewSet):
    queryset = Producent.objects.all()
    serializer_class = serializers.ProducentSerializer

    def get_queryset(self):
        queryset = self.queryset
        nazwa = self.request.query_params.get('nazwa', None)
        if nazwa is not None:
            print('wszedlem1')
            queryset = queryset.filter(nazwa__icontains=nazwa)
        return queryset


class ProduktViewsApi(viewsets.ModelViewSet):
    queryset = Produkt.objects.all()
    serializer_class = serializers.ProduktSerializer

    def get_queryset(self):
        queryset = self.queryset
        nazwa = self.request.query_params.get('nazwa', None)
        if nazwa is not None:
            print('wszedlem1')
            queryset = queryset.filter(nazwa__icontains=nazwa)
        return queryset


class TransakcjaViewsApi(viewsets.ModelViewSet):
    queryset = Transakcja.objects.all()
    serializer_class = serializers.TransakcjaSerializer


class FakturaViewsApi(viewsets.ModelViewSet):
    queryset = Faktura.objects.all()
    serializer_class = serializers.FakturaSerializer


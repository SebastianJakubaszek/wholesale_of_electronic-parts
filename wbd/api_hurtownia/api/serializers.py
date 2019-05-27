from rest_framework import serializers
from ..models import *


class HurtownieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hurtownie
        fields = ('nr_hurtowni', 'nazwa', 'miasto', 'ulica', 'nr_budynku', 'nr_lokalu', 'kod_pocztowy',
                  'data_zalozenia', 'imie_wlasciciela', 'nazwisko_wlasciciela')

class KontoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Konto
        fields = '__all__'

class KlientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Klient
        fields = '__all__'


class StanowiskaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stanowiska
        fields = '__all__'


class WynagrodzenieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wynagrodzenie
        fields = '__all__'


class PracownikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pracownik
        fields = '__all__'


class MagazynSerializer(serializers.ModelSerializer):
    class Meta:
        model = Magazyn
        fields = '__all__'


class DzialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dzial
        fields = '__all__'


class DostawcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dostawca
        fields = '__all__'


class ProducentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producent
        fields = '__all__'


class ProduktSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produkt
        fields = '__all__'

class TransakcjaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transakcja
        fields = '__all__'


class FakturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faktura
        fields = '__all__'
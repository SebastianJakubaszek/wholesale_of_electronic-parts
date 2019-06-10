from django.contrib.auth.models import User, AbstractUser
from django.db import models



class Hurtownie(models.Model):
    nr_hurtowni = models.AutoField(primary_key=True, editable=False)
    nazwa = models.CharField(max_length=50)
    miasto = models.CharField(max_length=30)
    ulica = models.CharField(max_length=30)
    nr_budynku = models.CharField(max_length=5)
    nr_lokalu = models.CharField(max_length=5, blank=True, null=True)
    kod_pocztowy = models.CharField(max_length=6)
    data_zalozenia = models.DateField()
    imie_wlasciciela = models.CharField(max_length=20)
    nazwisko_wlasciciela = models.CharField(max_length=30)

    class Meta:
        ordering = ('nr_hurtowni',)

    def __str__(self):
        return self.nazwa


class Konto(models.Model):
    nr_konta = models.AutoField(primary_key=True, editable=False)
    login = models.CharField(max_length=30, unique=True)
    haslo = models.CharField(max_length=30)

    def __str__(self):
        return self.login


class Klient(models.Model):
    nr_klienta = models.AutoField(primary_key=True, editable=False)
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=30)
    nr_telefonu = models.CharField(max_length=15)
    email = models.EmailField(max_length=30)
    firma = models.CharField(max_length=30, blank=True, null=True)
    nr_hurtowni = models.ForeignKey(Hurtownie, related_name="klient_hurtownia", on_delete=models.CASCADE)
    nr_konta = models.OneToOneField(Konto, related_name="klient_konto", on_delete=models.CASCADE, blank=True, null=True)


class Stanowiska(models.Model):
    nr_stanowiska = models.AutoField(primary_key=True, editable=False)
    stanowisko = models.CharField(max_length=30)
    opis = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.stanowisko



class Pracownik(models.Model):
    nr_pracownika = models.AutoField(primary_key=True, editable=False)
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=20)
    data_urodzenia = models.DateField()
    pesel = models.CharField(max_length=11, blank=True, null=True)
    data_zatrudnienia = models.DateField()
    nr_hurtowni = models.ForeignKey(Hurtownie, related_name='pracownik_hurtownia', on_delete=models.CASCADE)
    nr_konta = models.ForeignKey(Konto, related_name='pracownik_konto', on_delete=models.CASCADE, blank=True, null=True)
    nr_stanowiska = models.ForeignKey(Stanowiska, related_name='pracownik_stanowiska', on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.imie, self.nazwisko)



class Wynagrodzenie(models.Model):
    nr_wynagrodzenia = models.AutoField(primary_key=True, editable=False)
    data_wyplaty = models.DateField()
    pensja_pod = models.DecimalField(max_digits=10, decimal_places=2)
    premia = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    nr_pracownika = models.ForeignKey(Pracownik, related_name='wynagrodzenie_pracownik', on_delete=models.CASCADE)


class Magazyn(models.Model):
    nr_magazynu = models.AutoField(primary_key=True, editable=False)
    nazwa = models.CharField(max_length=50)
    data_zalozenia = models.DateField()
    miasto = models.CharField(max_length=30)
    ulica = models.CharField(max_length=30)
    nr_budynku = models.CharField(max_length=5)
    nr_lokalu = models.CharField(max_length=5, blank=True, null=True)
    kod_pocztowy = models.CharField(max_length=6)
    powierzchnia = models.FloatField(blank=True, null=True)
    nr_pracownika = models.ForeignKey(Pracownik, related_name='magazyn_pracownik', on_delete=models.CASCADE)
    nr_hurtowni = models.ForeignKey(Hurtownie, related_name='magazyn_hurtownia', on_delete=models.CASCADE)

    def __str__(self):
        return self.nazwa


class Dostawca(models.Model):
    nr_dostawcy = models.AutoField(primary_key=True, editable=False)
    nazwa = models.CharField(max_length=50)
    miasto = models.CharField(max_length=30)
    ulica = models.CharField(max_length=30)
    nr_budynku = models.CharField(max_length=5)
    nr_lokalu = models.CharField(max_length=5, blank=True, null=True)
    kod_pocztowy = models.CharField(max_length=6)
    nr_telefonu = models.CharField(max_length=15)
    email = models.EmailField(max_length=30)
    nr_hurtowni = models.ForeignKey(Hurtownie, related_name='dostawca_hurtownia', on_delete=models.CASCADE)

    def __str__(self):
        return self.nazwa


class Dzial(models.Model):
    nr_dzialu = models.AutoField(primary_key=True, editable=False)
    nazwa = models.CharField(max_length=30)
    opis = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.nazwa



class Producent(models.Model):
    nr_producenta = models.AutoField(primary_key=True, editable=False)
    nazwa = models.CharField(max_length=30)
    miasto = models.CharField(max_length=30)
    ulica = models.CharField(max_length=30)
    nr_budynku = models.CharField(max_length=5)
    nr_lokalu = models.CharField(max_length=5, blank=True, null=True)
    kod_pocztowy = models.CharField(max_length=6)
    nr_telefonu = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.nazwa



class Produkt(models.Model):
    nr_produktu = models.AutoField(primary_key=True, editable=False)
    nazwa = models.CharField(max_length=30)
    opis = models.TextField(max_length=500, blank=True, null=True)
    cena_zakupu = models.DecimalField(max_digits=10, decimal_places=2)
    cena_sprzedazy = models.DecimalField(max_digits=10, decimal_places=2)
    ilosc = models.IntegerField()
    nr_hurtowni = models.ForeignKey(Hurtownie, related_name='produkt_hurtownia', on_delete=models.CASCADE)
    nr_magazynu = models.ForeignKey(Magazyn, related_name='produkt_magazyn', on_delete=models.CASCADE)
    nr_producenta = models.ForeignKey(Producent, related_name='produkt_producent', on_delete=models.CASCADE)
    nr_dostawcy = models.ManyToManyField(Dostawca, related_name='produkt_dostawca')

    def __str__(self):
        return self.nazwa


class Transakcja(models.Model):
    nr_transakcji = models.IntegerField(primary_key=True, editable=False)
    data_transakcji = models.DateField()
    kwota = models.DecimalField(max_digits=10, decimal_places=2)
    nr_klienta = models.ForeignKey(Klient, related_name='transakcja_klient', on_delete=models.CASCADE)


class Faktura(models.Model):
    nr_faktury = models.IntegerField(primary_key=True, editable=False)
    data_wystawienia = models.DateField()
    kwota_netto = models.DecimalField(max_digits=10, decimal_places=2)
    kwota_brutto = models.DecimalField(max_digits=10, decimal_places=2)
    nr_transakcji = models.ForeignKey(Transakcja, related_name='faktura_transakcja', on_delete=models.CASCADE)












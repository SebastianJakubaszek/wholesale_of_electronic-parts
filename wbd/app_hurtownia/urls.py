from django.urls import path
from . import views


urlpatterns = [
    path('hurtownie/', views.pokaz_hurtownie, name="pokaz_hurtownie_list"),
    path('hurtownie/dodaj/', views.dodaj_hurtownie, name="dodaj_hurtownie"),
    path('hurtownie/<int:pk>', views.pokaz_hurtownie_detal, name="pokaz_hurtownie_detal"),
    path('hurtownie/usun/', views.usun_hurtownie, name="usun_hurtownie"),
    path('hurtownie/aktualizuj/<int:pk>', views.aktualizuj_hurtownie, name="aktualizuj_hurtownie"),
    path('klienci/', views.pokaz_klient, name="pokaz_klient_list"),
    path('klienci/<int:pk>', views.pokaz_klient_detail, name="pokaz_klient_detail"),
    path('klienci/rejestruj/', views.rejestruj_klient, name="rejestruj_klient"),
    path('produkty/', views.pokaz_produkt, name='pokaz_produkt_list'),
    path('produkty/<int:pk>', views.pokaz_produkt_detail, name= 'pokaz_produkt_detail'),
    path('producent/<int:pk>', views.pokaz_producent_detail, name= 'pokaz_producent_detail'),
    path('producenci/', views.pokaz_producent, name="pokaz_producent"),
    path('klienci/dodaj/', views.dodaj_klient, name='dodaj_klient'),
    path('klienci/usun/', views.usun_klienta, name='usun_klient'),
]

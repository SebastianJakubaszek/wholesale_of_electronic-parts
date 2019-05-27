from django.urls import path
from . import views


urlpatterns = [
    path('hurtownie/', views.pokaz_hurtownie, name="pokaz_hurtownie_list"),
    path('hurtownie/dodaj/', views.dodaj_hurtownie, name="dodaj_hurtownie"),
    path('hurtownie/<int:pk>', views.pokaz_hurtownie_detal, name="pokaz_hurtownie_detal"),
    path('hurtownie/usun/', views.usun_hurtownie, name="usun_hurtownie"),
    path('hurtownie/aktualizuj/<int:pk>', views.aktualizuj_hurtownie, name="aktualizuj_hurtownie"),
    path('klienci/', views.pokaz_klient, name="pokaz_klient_list"),
    path('klienci/<int:pk>', views.pokaz_klient_detal, name="pokaz_klient_detal"),
    path('klienci/rejestruj/', views.rejestruj_klient, name="rejestruj_klient"),

]

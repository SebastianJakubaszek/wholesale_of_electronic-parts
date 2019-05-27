from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('hurtownie', views.HurtownieViewsApi)
router.register('konta', views.KontoViewsApi)
router.register('klienci', views.KlientViewsApi)
router.register('stanowiska', views.StanowiskaViewsApi)
router.register('wynagrodzenia', views.WynagrodzenieViewsApi)
router.register('pracownicy', views.PracownikViewsApi)
router.register('magazyny', views.MagazynViewsApi)
router.register('dzialy', views.DzialViewsApi)
router.register('dostawcy', views.DostawcaViewsApi)
router.register('producenci', views.ProducentViewsApi)
router.register('produkty', views.ProduktViewsApi)
router.register('transakcje', views.TransakcjaViewsApi)
router.register('faktury', views.FakturaViewsApi)

urlpatterns = [
   path('', include(router.urls)),
]

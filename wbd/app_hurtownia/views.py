from django.shortcuts import render
from .forms import HurtowniaForm, KlientForm, HurtowniaFormUsun, HurtowniaFormAktualizuj, KlientFormRegister
import requests


def pokaz_hurtownie(request):
    response = requests.get('http://127.0.0.1:8000/api/hurtownie').json()
    return render(request, 'hurtownia_list.html', {'hurtownie': response})


def pokaz_hurtownie_detal(request, pk):
    response = requests.get('http://127.0.0.1:8000/api/hurtownie/{}'.format(pk)).json()
    return render(request, 'hurtownia_detail.html', {'hurtownia': response})


def dodaj_hurtownie(request):
    if request.method == "GET":
        hurtownia_form = HurtowniaForm()
        return render(request, 'hurtownia_dodaj.html', {'hurtownia_form': hurtownia_form})
    elif request.method == "POST":
        request_post = HurtowniaForm(data=request.POST)
        if request_post.is_valid():
            request_post = request_post.cleaned_data
        response = requests.post('http://127.0.0.1:8000/api/hurtownie/', data=request_post)
        if response.status_code == 201:
            status = "Dodano hurtownie"
        else:
            status = "Bład podczas dodawnia"
        return render(request, 'hurtownia_dodaj_odpowiedz.html', {"status": status})


def usun_hurtownie(request):
    if request.method == "GET":
        response = requests.get('http://127.0.0.1:8000/api/hurtownie').json()
        hurtownia_form = HurtowniaFormUsun(hurtownie=response)
        return render(request, 'hurtownia_usun.html', {'hurtownia_form': hurtownia_form})
    elif request.method == "POST":
        request_post = HurtowniaFormUsun(data=request.POST)
        if request_post.is_valid():
            request_post = request_post.cleaned_data
        response = requests.delete('http://127.0.0.1:8000/api/hurtownie/{}'.format(request_post['nazwa_hurtowni']))
        if response.status_code == 204:
            status = "Usunięto hurtownie pomyślnie"
        else:
            status = "Bład podczas usunięcia hurtowni"
        return render(request, 'hurtownia_dodaj_odpowiedz.html', {"status": status}, status=response.status_code)


def aktualizuj_hurtownie(request, pk):
    if request.method == "GET":
        response = requests.get('http://127.0.0.1:8000/api/hurtownie/{}'.format(pk)).json()
        fill_data = {}
        for key, count in response.items():
            if not key == "nr_hurtowni":
                fill_data[key] = count
        hurtownia_form = HurtowniaFormAktualizuj(initial=fill_data)
        return render(request, 'hurtownia_aktualizuj.html', {'hurtownia_form': hurtownia_form,
                                                             'hurtownia_name': fill_data['nazwa']})

    elif request.method == "POST":
        request_post = HurtowniaFormAktualizuj(data=request.POST)
        if request_post.is_valid():
            request_post = request_post.cleaned_data
        patch = False
        request_post_dict = {}
        for key, count in request_post.items():
            if count == '':
                if not key is 'nr_lokalu':
                    patch = True
                else:
                    request_post_dict[key] = count
            else:
                request_post_dict[key] = count
        if patch:
            response = requests.patch('http://127.0.0.1:8000/api/hurtownie/{}/'.format(pk), data=request_post_dict)
        else:
            response = requests.put('http://127.0.0.1:8000/api/hurtownie/{}/'.format(pk), data=request_post_dict)
        if response.status_code == 200:
            status = "Zaktualizowano hurtownie"
        else:
            status = "Bład podczas aktualizacji"
        return render(request, 'hurtownia_dodaj_odpowiedz.html', {"status": status})


def pokaz_klient(request):
    imie = request.GET.get('imie')
    nazwisko = request.GET.get('nazwisko')
    response = requests.get('http://127.0.0.1:8000/api/klienci/?imie={}&nazwisko={}'.format(imie, nazwisko)).json()
    return render(request, 'klient_list.html', {'klienci': response})


def pokaz_klient_detal(request, pk):
    response = requests.get('http://127.0.0.1:8000/api/klienci/{}'.format(pk)).json()
    response_hurtownia = requests.get('http://127.0.0.1:8000/api/hurtownie/{}'.format(response['nr_hurtowni'])).json()
    if not response['nr_konta'] is None:
        response_konto = requests.get('http://127.0.0.1:8000/api/konta/{}'.format(response['nr_konta'])).json()
    else:
        response_konto = {'login': '', 'haslo': ''}
    return render(request, 'klient_detail.html', {'klient': response,
                                                  'hurtownia': response_hurtownia,
                                                  'konto': response_konto})


def dodaj_klient(request):
    if request.method == "GET":
        response = requests.get('http://127.0.0.1:8000/api/hurtownie').json()
        klient_form = KlientForm(hurtownie=response)
        return render(request, 'klient_dodaj.html', {'klient_form': klient_form})
    elif request.method == "POST":
        request_post = KlientForm(data=request.POST)
        if request_post.is_valid():
            request_post = request_post.cleaned_data
        request_post['nr_hurtowni'] = request_post.pop('nazwa_hurtowni')
        response = requests.post('http://127.0.0.1:8000/api/klienci/', data=request_post)
        if response.status_code == 201:
            status = "Dodano hurtownie"
        else:
            status = "Bład podczas dodawnia"
        return render(request, 'hurtownia_dodaj_odpowiedz.html', {"status": status})

def rejestruj_klient(request):
    if request.method == "POST":
        klient_form = KlientFormRegister(data=request.POST)
        if klient_form.is_valid():
            request_post_konto ={}
            request_post_klient ={}
            request_post = klient_form.cleaned_data
            for key, count in request_post.items():
                if (key == 'login' or key == 'haslo'):
                    request_post_konto[key]=count
                else:
                    request_post_klient[key]=count
            response = requests.post('http://127.0.0.1:8000/api/konta/', data=request_post_konto)
            if response.status_code == 201:
                response_konto=requests.get('http://127.0.0.1:8000/api/konta').json()
                for i in response_konto:
                    if i['login'] == request_post_konto['login']:
                        id_konta = i['nr_konta']
                        request_post_klient['nr_konta'] =id_konta
                response = requests.post('http://127.0.0.1:8000/api/klienci/', data=request_post_klient)
                if response.status_code == 201:
                    status = "Poprawna rejestracja konta"
                else:
                    response = requests.delete('http://127.0.0.1:8000/api/konta/{}'.format(request_post_klient['nr_konta']))
                    status = "Nie udalo sie zarejestrować konta"
                return render(request, 'hurtownia_dodaj_odpowiedz.html', {"status": status})
            else:
                status = "Nie udalo sie zarejestrować konta"
                return render(request, 'hurtownia_dodaj_odpowiedz.html', {"status": status})
    else:
        response = requests.get('http://127.0.0.1:8000/api/hurtownie').json()
        response_konto = requests.get('http://127.0.0.1:8000/api/konta').json()
        klient_form = KlientFormRegister(hurtownie=response, konta=response_konto)
    return render(request, 'klient_rejestracja.html', {'klient_form': klient_form})

def wyszukaj_klient(request,imie,nazwisko):
    print('wszedlem')
    response = requests.get('http://127.0.0.1:8000/api/klienci?imie@{}&nazwisko@{}'.format(imie,nazwisko)).json()
    return render(request, 'klient_list.html', {'klienci': response})
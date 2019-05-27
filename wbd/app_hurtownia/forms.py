from django import forms


class HurtowniaForm(forms.Form):
    nazwa = forms.CharField(max_length=50)
    miasto = forms.CharField(max_length=30)
    ulica = forms.CharField(max_length=30)
    nr_budynku = forms.CharField(max_length=5)
    nr_lokalu = forms.CharField(max_length=5, required=False)
    kod_pocztowy = forms.CharField(max_length=6)
    data_zalozenia = forms.DateField(widget=forms.widgets.DateTimeInput(attrs={'type':'date'}))
    imie_wlasciciela = forms.CharField(max_length=20)
    nazwisko_wlasciciela = forms.CharField(max_length=30)

class HurtowniaFormUsun(forms.Form):
    choices = []
    def __init__(self,*args,**kwargs):
        if 'request' in kwargs:
            request = kwargs.pop('request')
            self.user = request.user
        if 'hurtownie' in kwargs:
            for hurtownia in kwargs.pop('hurtownie'):
                self.choices.append((hurtownia['nr_hurtowni'], hurtownia['nazwa']))
        super(HurtowniaFormUsun, self).__init__(*args, **kwargs)
        self.fields['nazwa_hurtowni'] = forms.ChoiceField(choices=tuple(self.choices))

    nazwa_hurtowni = forms.ChoiceField()

class HurtowniaFormAktualizuj(forms.Form):

    nazwa = forms.CharField(max_length=50, required=False)
    miasto = forms.CharField(max_length=30, required=False)
    ulica = forms.CharField(max_length=30, required=False)
    nr_budynku = forms.CharField(max_length=5, required=False)
    nr_lokalu = forms.CharField(max_length=5, required=False)
    kod_pocztowy = forms.CharField(max_length=6, required=False)
    data_zalozenia = forms.DateField(widget=forms.widgets.DateTimeInput(attrs={'type': 'date'}), required=False)
    imie_wlasciciela = forms.CharField(max_length=20, required=False)
    nazwisko_wlasciciela = forms.CharField(max_length=30, required=False)


class KlientForm(forms.Form):
    choices = []
    def __init__(self,*args,**kwargs):
        if 'request' in kwargs:
            request = kwargs.pop('request')
            self.user = request.user
        if 'hurtownie' in kwargs:
            for hurtownia in kwargs.pop('hurtownie'):
                self.choices.append((hurtownia['nr_hurtowni'], hurtownia['nazwa']))
        super(KlientForm, self).__init__(*args, **kwargs)
        self.fields['nazwa_hurtowni'] = forms.ChoiceField(choices=tuple(self.choices))

    imie = forms.CharField(max_length=20)
    nazwisko = forms.CharField(max_length=30)
    nr_telefonu = forms.CharField(max_length=15)
    email = forms.EmailField(max_length=30)
    firma = forms.CharField(max_length=30, required=False)
    nazwa_hurtowni = forms.ChoiceField()
    nr_konta = forms.IntegerField(required=False)

class KlientFormRegister(forms.Form):
    choices = []
    konta = []
    def __init__(self,*args,**kwargs):
        if 'request' in kwargs:
            request = kwargs.pop('request')
            self.user = request.user
        if 'hurtownie' in kwargs:
            for hurtownia in kwargs.pop('hurtownie'):
                self.choices.append((hurtownia['nr_hurtowni'], hurtownia['nazwa']))
        if 'konta' in kwargs:
            for konto in kwargs.pop('konta'):
                self.konta.append(konto['login'])
        super(KlientFormRegister, self).__init__(*args, **kwargs)
        self.fields['nr_hurtowni'] = forms.ChoiceField(choices=tuple(self.choices))


    login = forms.CharField(max_length=30)
    haslo = forms.CharField(label="Hasło",
                               widget=forms.PasswordInput,
                               max_length=30)
    haslo2 = forms.CharField(label="Powtórz hasło",
                                widget=forms.PasswordInput,
                                max_length=30)
    imie = forms.CharField(max_length=20)
    nazwisko = forms.CharField(max_length=30)
    nr_telefonu = forms.CharField(max_length=15)
    email = forms.EmailField(max_length=30)
    firma = forms.CharField(max_length=30, required=False)
    nr_hurtowni = forms.ChoiceField()

    def clean_haslo2(self):
        cd = self.cleaned_data
        if cd['haslo'] != cd['haslo2']:
            raise forms.ValidationError('Hasła nie sa identyczne.')
        return cd['haslo2']

    def clean_login(self):
        cd = self.cleaned_data
        if cd['login'] in self.konta:
            raise forms.ValidationError('Login juz istnieje')
        return cd['login']

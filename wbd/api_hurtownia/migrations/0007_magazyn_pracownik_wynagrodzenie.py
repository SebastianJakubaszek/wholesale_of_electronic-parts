# Generated by Django 2.2.1 on 2019-05-19 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_hurtownia', '0006_stanowiska'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pracownik',
            fields=[
                ('nr_pracownika', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('imie', models.CharField(max_length=20)),
                ('nazwisko', models.CharField(max_length=20)),
                ('data_urodzenia', models.DateField()),
                ('pesel', models.CharField(blank=True, max_length=11, null=True)),
                ('data_zatrudnienia', models.DateField()),
                ('nr_hurtowni', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pracownik_hurtownia', to='api_hurtownia.Hurtownie')),
                ('nr_konta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pracownik_konto', to='api_hurtownia.Konto')),
                ('nr_stanowiska', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pracownik_stanowiska', to='api_hurtownia.Stanowiska')),
            ],
        ),
        migrations.CreateModel(
            name='Wynagrodzenie',
            fields=[
                ('nr_wynagrodzenia', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('data_wyplaty', models.DateField()),
                ('pensja_pod', models.DecimalField(decimal_places=2, max_digits=10)),
                ('premia', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('nr_pracownika', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wynagrodzenie_pracownik', to='api_hurtownia.Pracownik')),
            ],
        ),
        migrations.CreateModel(
            name='Magazyn',
            fields=[
                ('nr_magazynu', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('nazwa', models.CharField(max_length=50)),
                ('data_zalozenia', models.DateField()),
                ('miasto', models.CharField(max_length=30)),
                ('ulica', models.CharField(max_length=30)),
                ('nr_budynku', models.CharField(max_length=5)),
                ('nr_lokalu', models.CharField(blank=True, max_length=5, null=True)),
                ('kod_pocztowy', models.CharField(max_length=6)),
                ('powierzchnia', models.FloatField(blank=True, null=True)),
                ('nr_hurtowni', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='magazyn_hurtownia', to='api_hurtownia.Hurtownie')),
                ('nr_pracownika', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='magazyn_pracownik', to='api_hurtownia.Pracownik')),
            ],
        ),
    ]

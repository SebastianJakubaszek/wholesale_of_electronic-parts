# Generated by Django 2.2.1 on 2019-05-27 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_hurtownia', '0012_auto_20190528_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produkt',
            name='opis',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
# Generated by Django 2.2.1 on 2019-05-31 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_hurtownia', '0013_auto_20190528_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produkt',
            name='nr_produktu',
            field=models.AutoField(editable=False, primary_key=True, serialize=False),
        ),
    ]

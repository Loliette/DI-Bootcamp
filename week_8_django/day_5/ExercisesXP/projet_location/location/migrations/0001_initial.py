# Generated by Django 4.1.3 on 2022-12-03 13:40

import datetime
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenom', models.CharField(max_length=100)),
                ('nom', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('numero', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('adresse', models.CharField(max_length=100)),
                ('ville', models.CharField(max_length=100)),
                ('pays', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TailleVehicule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TypeVehicule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(default=datetime.date(2022, 12, 3))),
                ('prix', models.DecimalField(decimal_places=2, max_digits=6)),
                ('taille', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.taillevehicule')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.typevehicule')),
            ],
        ),
        migrations.CreateModel(
            name='TarifLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taux', models.DecimalField(decimal_places=2, max_digits=6)),
                ('taille_vehicule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.taillevehicule')),
                ('type_vehicule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.typevehicule')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_location', models.DateField(default=datetime.date(2022, 12, 3))),
                ('date_retour', models.DateField(default=datetime.date(2022, 12, 3))),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.client')),
                ('vehicule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.vehicule')),
            ],
        ),
    ]

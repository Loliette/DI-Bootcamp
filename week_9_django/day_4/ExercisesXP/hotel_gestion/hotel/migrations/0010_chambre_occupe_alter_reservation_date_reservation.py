# Generated by Django 4.1.4 on 2022-12-18 11:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0009_alter_chambre_prix_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='chambre',
            name='occupe',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='date_reservation',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 18, 11, 19, 48, 8203)),
        ),
    ]

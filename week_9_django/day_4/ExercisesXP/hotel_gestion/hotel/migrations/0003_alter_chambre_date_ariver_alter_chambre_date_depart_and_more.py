# Generated by Django 4.1.4 on 2022-12-18 11:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_remove_chambre_date_reservation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chambre',
            name='date_ariver',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='chambre',
            name='date_depart',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='chambre',
            name='date_disponible',
            field=models.DateField(default=datetime.date(2022, 12, 18)),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='date_reservation',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 18, 11, 0, 8, 514570)),
        ),
    ]

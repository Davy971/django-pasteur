# Generated by Django 2.1.5 on 2019-02-04 22:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20190131_1602'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feuille_calcul',
            name='date_mise_sous_essai',
        ),
        migrations.AddField(
            model_name='feuille_calcul',
            name='date_analyse',
            field=models.DateField(default=datetime.datetime(2019, 2, 4, 22, 19, 59, 71691)),
        ),
    ]
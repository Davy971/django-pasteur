# Generated by Django 2.1.5 on 2019-02-14 15:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0035_auto_20190214_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='feuille_calcul',
            name='date_creation',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

# Generated by Django 2.1.7 on 2019-05-21 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0050_remove_feuille_calcul_etalonnage'),
    ]

    operations = [
        migrations.AddField(
            model_name='feuille_calcul',
            name='etalonnage',
            field=models.CharField(default='null', max_length=100, verbose_name='Etalonnage'),
        ),
    ]

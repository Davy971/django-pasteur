# Generated by Django 2.1.7 on 2019-05-21 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0049_auto_20190506_2246'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feuille_calcul',
            name='etalonnage',
        ),
    ]

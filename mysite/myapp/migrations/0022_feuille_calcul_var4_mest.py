# Generated by Django 2.1.5 on 2019-02-07 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_auto_20190207_0857'),
    ]

    operations = [
        migrations.AddField(
            model_name='feuille_calcul',
            name='var4_mest',
            field=models.CharField(default='NULL', max_length=60, verbose_name='date de préparation de la solution de cellulose microcristalline'),
        ),
    ]

# Generated by Django 2.1.5 on 2019-02-12 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0033_auto_20190212_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='feuille_calcul',
            name='var10_dco',
            field=models.CharField(default='NULL', max_length=100, verbose_name='Blanc'),
        ),
    ]
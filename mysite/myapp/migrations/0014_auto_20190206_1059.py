# Generated by Django 2.1.5 on 2019-02-06 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_auto_20190206_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analyse',
            name='var1_kmno4',
            field=models.CharField(max_length=60, verbose_name='V0'),
        ),
        migrations.AlterField(
            model_name='analyse',
            name='var2_kmno4',
            field=models.CharField(max_length=60, verbose_name='V1'),
        ),
        migrations.AlterField(
            model_name='analyse',
            name='var3_kmno4',
            field=models.CharField(max_length=60, verbose_name='V2'),
        ),
        migrations.AlterField(
            model_name='analyse',
            name='var4_kmno4',
            field=models.CharField(max_length=60, verbose_name='Facteur dilution'),
        ),
        migrations.AlterField(
            model_name='analyse',
            name='var5_kmno4',
            field=models.CharField(max_length=60, verbose_name='Resultat en mg/L'),
        ),
    ]

# Generated by Django 3.0.8 on 2020-12-01 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablaagenda',
            name='apellido',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Apellido'),
        ),
        migrations.AlterField(
            model_name='tablaagenda',
            name='nombre',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Nombre'),
        ),
    ]

# Generated by Django 4.2.4 on 2023-11-13 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiendaApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mesas',
            name='estado',
            field=models.CharField(max_length=50),
        ),
    ]
# Generated by Django 4.2.4 on 2023-11-14 19:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tiendaApp', '0007_alter_productos_options_productos_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
# Generated by Django 5.0.2 on 2024-02-09 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Producto',
        ),
        migrations.DeleteModel(
            name='ProductoCategoria',
        ),
    ]

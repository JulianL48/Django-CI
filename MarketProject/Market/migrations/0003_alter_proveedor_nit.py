# Generated by Django 5.0.7 on 2024-07-29 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Market', '0002_proveedor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='nit',
            field=models.CharField(max_length=13),
        ),
    ]

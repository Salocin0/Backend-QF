# Generated by Django 4.2.1 on 2023-07-11 21:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='contraseña',
            field=models.CharField(max_length=128, validators=[django.core.validators.MinLengthValidator(6)]),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='correoElectronico',
            field=models.EmailField(max_length=50, unique=True),
        ),
    ]

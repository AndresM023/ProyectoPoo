# Generated by Django 4.1.1 on 2022-09-25 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuenta_cobrar', '0019_remove_pagodeuda_deuda_alter_pagodeuda_cabecera'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cabecera',
            name='meses_a_diferir',
            field=models.IntegerField(),
        ),
    ]

# Generated by Django 4.1.3 on 2022-11-05 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goles', '0002_goles_fecha_ref_alter_goles_fecha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goles',
            name='fecha_ref',
        ),
    ]

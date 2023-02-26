# Generated by Django 4.1.3 on 2022-11-05 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('equipo', models.CharField(max_length=30)),
                ('rival', models.CharField(max_length=30)),
                ('minuto', models.IntegerField()),
                ('parcial', models.CharField(max_length=30)),
            ],
        ),
    ]

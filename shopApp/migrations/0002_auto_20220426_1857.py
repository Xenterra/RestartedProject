# Generated by Django 3.1.3 on 2022-04-26 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamelist',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AlterModelTable(
            name='gamedetails',
            table='gameDetails',
        ),
        migrations.AlterModelTable(
            name='gamelist',
            table='gameList',
        ),
    ]

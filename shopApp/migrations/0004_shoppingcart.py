# Generated by Django 3.1.3 on 2022-04-30 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0003_auto_20220429_1514'),
    ]

    operations = [
        migrations.CreateModel(
            name='shoppingCart',
            fields=[
                ('uniqueid', models.IntegerField(primary_key=True, serialize=False)),
                ('gameID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shopApp.gamelist')),
            ],
        ),
    ]

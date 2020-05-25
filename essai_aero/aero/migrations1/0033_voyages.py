# Generated by Django 3.0.4 on 2020-04-28 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aero', '0032_delete_voyages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voyages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compagnie', models.CharField(max_length=1000)),
                ('ville_depart', models.CharField(max_length=1000)),
                ('aeroport_depart', models.CharField(max_length=1000)),
                ('ville_arrive', models.CharField(max_length=1000)),
                ('aeroport_arrive', models.CharField(max_length=1000)),
                ('date', models.DateField(max_length=1000)),
                ('price', models.IntegerField(default=0)),
                ('places', models.IntegerField(default=0)),
            ],
        ),
    ]
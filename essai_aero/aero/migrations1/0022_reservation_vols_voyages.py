# Generated by Django 3.0.4 on 2020-04-14 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aero', '0021_delete_vols'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_voyage', models.IntegerField(default=0)),
                ('reference_client', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Vols',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airline', models.CharField(max_length=1000)),
                ('departure', models.CharField(max_length=1000)),
                ('arrival', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Voyages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compagnie', models.CharField(max_length=1000)),
                ('depart', models.CharField(max_length=1000)),
                ('arrive', models.CharField(max_length=1000)),
                ('date', models.DateField(max_length=1000)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
    ]
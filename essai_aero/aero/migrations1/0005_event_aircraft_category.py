# Generated by Django 3.0.4 on 2020-04-02 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aero', '0004_auto_20200402_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='aircraft_category',
            field=models.CharField(default=0, max_length=1000),
        ),
    ]

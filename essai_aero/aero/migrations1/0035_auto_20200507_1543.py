# Generated by Django 3.0.2 on 2020-05-07 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aero', '0034_statistics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistics',
            name='number',
            field=models.IntegerField(default=0),
        ),
    ]
# Generated by Django 3.0.4 on 2020-04-14 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aero', '0019_auto_20200415_0103'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vols',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airline', models.CharField(max_length=1000)),
                ('departure', models.CharField(max_length=1000)),
                ('arrival', models.CharField(max_length=1000)),
            ],
        ),
    ]

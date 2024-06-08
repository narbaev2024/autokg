# Generated by Django 5.0.6 on 2024-05-27 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_store', '0003_car_engine'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='car_name_en',
            field=models.CharField(max_length=16, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='car',
            name='car_name_ky',
            field=models.CharField(max_length=16, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='car',
            name='car_name_ru',
            field=models.CharField(max_length=16, null=True, unique=True),
        ),
    ]

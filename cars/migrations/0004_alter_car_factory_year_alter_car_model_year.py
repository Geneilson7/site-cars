# Generated by Django 4.2.6 on 2023-11-02 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_car_photo_car_plate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='factory_year',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='model_year',
            field=models.DateField(blank=True, null=True),
        ),
    ]

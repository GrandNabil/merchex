# Generated by Django 4.2.4 on 2023-09-03 13:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0006_alter_listings_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='year',
            field=models.IntegerField(blank=True, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2021)]),
        ),
    ]
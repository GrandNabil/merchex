# Generated by Django 4.2.4 on 2023-09-03 12:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_band_active_band_biography_band_genre_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=1000)),
                ('sold', models.BooleanField(default=True)),
                ('year', models.IntegerField(blank=True, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2021)])),
                ('type', models.CharField(choices=[('RCD', 'Records'), ('CLT', 'Clothing'), ('PTR', 'Posters'), ('MLS', 'Miscellaneous')], max_length=5)),
            ],
        ),
    ]
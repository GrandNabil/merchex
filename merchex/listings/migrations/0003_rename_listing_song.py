# Generated by Django 4.2.4 on 2023-08-30 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_listing'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Listing',
            new_name='Song',
        ),
    ]

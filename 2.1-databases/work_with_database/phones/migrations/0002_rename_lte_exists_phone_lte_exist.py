# Generated by Django 4.1.7 on 2023-04-02 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='phone',
            old_name='lte_exists',
            new_name='lte_exist',
        ),
    ]

# Generated by Django 4.2 on 2023-05-01 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='records',
            old_name='mri',
            new_name='reports',
        ),
    ]

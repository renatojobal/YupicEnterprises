# Generated by Django 4.0.1 on 2022-01-26 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='kgPerDolar',
            new_name='kgPerDollar',
        ),
    ]

# Generated by Django 4.0.1 on 2022-01-26 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('thumnail', models.ImageField(blank=True, upload_to='media/thumnails/')),
                ('kgPerDolar', models.FloatField(blank=True, default=0.0)),
            ],
        ),
    ]

# Generated by Django 5.0.1 on 2024-01-23 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ponte', '0002_alter_dispositivo_id_dispositivo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='red',
            name='latitud',
            field=models.CharField(default=42, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='red',
            name='longitud',
            field=models.CharField(default=-6, max_length=20),
            preserve_default=False,
        ),
    ]
# Generated by Django 5.0.1 on 2024-02-03 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ponte', '0008_ancla'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dispositivo',
            name='localizacion',
        ),
        migrations.RemoveField(
            model_name='dispositivo',
            name='tipo',
        ),
    ]
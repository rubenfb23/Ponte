# Generated by Django 5.0.1 on 2024-02-03 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ponte', '0009_remove_dispositivo_localizacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ancla',
            name='estado',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='dispositivo',
            name='estado',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='grupo',
            name='estado',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='estado',
            field=models.BooleanField(),
        ),
    ]

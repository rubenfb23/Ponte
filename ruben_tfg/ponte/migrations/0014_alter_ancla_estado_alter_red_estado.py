# Generated by Django 5.0.1 on 2024-02-03 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ponte', '0013_remove_servicio_tipo_alter_ancla_tipo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ancla',
            name='estado',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='red',
            name='estado',
            field=models.BooleanField(),
        ),
    ]

# Generated by Django 5.0.1 on 2024-02-01 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ponte', '0006_servicio_puerto'),
    ]

    operations = [
        migrations.AddField(
            model_name='dispositivo',
            name='mac',
            field=models.CharField(default='75:df:1e:be:35:12', max_length=20),
            preserve_default=False,
        ),
    ]
# Generated by Django 4.2.6 on 2023-12-10 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0011_device_main'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='main',
            field=models.BooleanField(default=False),
        ),
    ]
# Generated by Django 4.2.6 on 2023-12-04 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0011_rename_susspend_agent_suspend'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.PositiveIntegerField(max_length=8, null=True, unique=True),
        ),
    ]

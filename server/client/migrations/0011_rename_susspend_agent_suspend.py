# Generated by Django 4.2.6 on 2023-11-24 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0010_agent_agent_id_alter_agent_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agent',
            old_name='susspend',
            new_name='suspend',
        ),
    ]

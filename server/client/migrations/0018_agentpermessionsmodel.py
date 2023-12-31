# Generated by Django 4.2.6 on 2023-12-15 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0012_alter_device_main'),
        ('client', '0017_otp_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgentPermessionsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manage_agents', models.BooleanField(default=False)),
                ('manage_devices', models.BooleanField(default=False)),
                ('check_historic', models.BooleanField(default=False)),
                ('config_device', models.BooleanField(default=False)),
                ('agent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.user')),
                ('device_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='administration.device')),
            ],
        ),
    ]

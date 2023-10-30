# Generated by Django 4.2.6 on 2023-10-30 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0002_delete_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('email', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=255)),
                ('user_name', models.CharField(max_length=30)),
                ('role', models.CharField(choices=[('admin', 'ADMIN'), ('agent', 'AGENT')], max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
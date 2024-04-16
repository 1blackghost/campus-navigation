# Generated by Django 5.0.2 on 2024-02-16 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('email_verified', models.BooleanField(default=False)),
                ('additional_params', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
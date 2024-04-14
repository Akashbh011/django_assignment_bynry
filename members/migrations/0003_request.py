# Generated by Django 4.2.5 on 2024-04-12 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_servicerequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('service_type', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]

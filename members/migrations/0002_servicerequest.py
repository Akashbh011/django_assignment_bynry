# Generated by Django 4.2.5 on 2024-04-12 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('contactnum', models.CharField(max_length=20)),
                ('attachment', models.ImageField(upload_to='attachments/')),
            ],
        ),
    ]

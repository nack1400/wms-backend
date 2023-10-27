# Generated by Django 4.2.6 on 2023-10-27 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SystemConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pallet_number', models.PositiveIntegerField(default=1)),
                ('inbound_number', models.PositiveIntegerField(default=1)),
                ('outbound_number', models.PositiveIntegerField(default=1)),
            ],
            options={
                'verbose_name': 'System Configuration',
            },
        ),
        migrations.DeleteModel(
            name='SequenceNumber',
        ),
    ]

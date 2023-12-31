# Generated by Django 4.2.6 on 2023-10-31 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lot_number', models.CharField(max_length=50)),
                ('lb_weight', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('kg_weight', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('location_type', models.CharField(choices=[('freezer', 'Freezer'), ('cooler', 'Cooler'), ('dry', 'Dry')], max_length=10)),
                ('pack_date', models.DateField(blank=True, null=True)),
                ('expiration_date', models.DateField(blank=True, null=True)),
                ('memo', models.TextField(blank=True, null=True)),
                ('initial_quantity', models.PositiveIntegerField(default=0)),
                ('current_quantity', models.PositiveIntegerField(default=0)),
                ('picked_quantity', models.PositiveIntegerField(default=0)),
                ('released_quantity', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='InventoryTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('transaction_type', models.CharField(max_length=25)),
                ('quantity', models.PositiveIntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

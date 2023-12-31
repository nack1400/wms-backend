# Generated by Django 4.2.6 on 2023-10-31 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('warehouses', '0001_initial'),
        ('handling_units', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalpallet',
            name='bin_location',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='warehouses.binlocation'),
        ),
        migrations.AddField(
            model_name='pallet',
            name='bin_location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='warehouses.binlocation'),
        ),
    ]

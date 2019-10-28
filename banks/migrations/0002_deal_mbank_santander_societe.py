# Generated by Django 2.2.2 on 2019-06-07 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('deal_number', models.AutoField(primary_key=True, serialize=False)),
                ('deal_date', models.DateField(null=True)),
                ('value_date', models.DateField(null=True)),
                ('deal_kind', models.CharField(max_length=20, null=True)),
                ('currency', models.CharField(max_length=3, null=True)),
                ('currency_cross', models.CharField(max_length=7, null=True)),
                ('side', models.CharField(max_length=20, null=True)),
                ('counterparty', models.CharField(max_length=30, null=True)),
                ('counterparty_another', models.CharField(max_length=30, null=True)),
                ('amount_in_base_cur', models.FloatField(null=True)),
                ('amount_in_side_cur', models.FloatField(null=True)),
                ('exchange_rate', models.FloatField(null=True)),
                ('interest_rate', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='mBank',
            fields=[
                ('date', models.DateField(primary_key=True, serialize=False)),
                ('start_balance', models.FloatField(default=0)),
                ('end_balance', models.FloatField(default=0)),
                ('inflows', models.FloatField(default=0)),
                ('outflows', models.FloatField(default=0)),
                ('transfer_in', models.FloatField(default=0)),
                ('transfer_out', models.FloatField(default=0)),
                ('depo', models.FloatField(default=0)),
                ('interest', models.FloatField(default=0)),
                ('reconciliation', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Santander',
            fields=[
                ('date', models.DateField(primary_key=True, serialize=False)),
                ('start_balance', models.FloatField(null=True)),
                ('end_balance', models.FloatField(null=True)),
                ('inflows', models.FloatField(null=True)),
                ('outflows', models.FloatField(null=True)),
                ('transfer_in', models.FloatField(null=True)),
                ('transfer_out', models.FloatField(null=True)),
                ('depo', models.FloatField(null=True)),
                ('interest', models.FloatField(null=True)),
                ('reconciliation', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Societe',
            fields=[
                ('date', models.DateField(primary_key=True, serialize=False)),
                ('start_balance', models.FloatField(null=True)),
                ('end_balance', models.FloatField(null=True)),
                ('inflows', models.FloatField(null=True)),
                ('outflows', models.FloatField(null=True)),
                ('transfer_in', models.FloatField(null=True)),
                ('transfer_out', models.FloatField(null=True)),
                ('depo', models.FloatField(null=True)),
                ('interest', models.FloatField(null=True)),
                ('reconciliation', models.FloatField(null=True)),
            ],
        ),
    ]
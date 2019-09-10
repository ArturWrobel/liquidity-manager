# Generated by Django 2.2.2 on 2019-06-13 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0006_auto_20190613_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deals',
            name='counterparty',
            field=models.CharField(choices=[('Citi', 'Citi'), ('mBank', ' mBank'), ('Societe', 'Societe'), ('Santander', 'Santander')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='deals',
            name='currency_base',
            field=models.CharField(choices=[('PLN', 'PLN'), ('EUR', 'EUR'), ('USD', 'USD')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='deals',
            name='currency_cross',
            field=models.CharField(choices=[('EUR/PLN', 'EUR/PLN'), ('USD/PLN', 'USD/PLN'), ('EUR/USD', 'EUR/USD')], max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='deals',
            name='currency_side',
            field=models.CharField(choices=[('PLN', 'PLN'), ('EUR', 'EUR'), ('USD', 'USD')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='deals',
            name='deal_kind',
            field=models.CharField(choices=[('DEPO', 'DEPO'), ('TXFR', 'TXFR'), ('FX_BUY', 'FX_BUY'), ('FX_SELL', 'FX_SELL')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='deals',
            name='side',
            field=models.CharField(choices=[('BUY', 'BUY'), ('SELL', 'SELL')], max_length=20, null=True),
        ),
    ]

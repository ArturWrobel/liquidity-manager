# Generated by Django 2.2.2 on 2019-06-25 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0014_auto_20190625_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deals',
            name='amount_in_base_cur',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='deals',
            name='amount_in_side_cur',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='deals',
            name='currency_base',
            field=models.CharField(blank=True, choices=[('PLN', 'PLN'), ('EUR', 'EUR'), ('USD', 'USD')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='deals',
            name='currency_cross',
            field=models.CharField(blank=True, choices=[('EUR/PLN', 'EUR/PLN'), ('USD/PLN', 'USD/PLN'), ('EUR/USD', 'EUR/USD')], max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='deals',
            name='currency_side',
            field=models.CharField(blank=True, choices=[('PLN', 'PLN'), ('EUR', 'EUR'), ('USD', 'USD')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='deals',
            name='exchange_rate',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='deals',
            name='interest_rate',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='deals',
            name='interest_rate_amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='deals',
            name='side',
            field=models.CharField(blank=True, choices=[('BUY', 'BUY'), ('SELL', 'SELL')], max_length=20, null=True),
        ),
    ]

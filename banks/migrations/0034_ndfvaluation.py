# Generated by Django 2.2.2 on 2019-12-13 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0033_auto_20191201_2033'),
    ]

    operations = [
        migrations.CreateModel(
            name='NDFVALUATION',
            fields=[
                ('num', models.AutoField(primary_key=True, serialize=False)),
                ('valuation_date', models.DateField(null=True)),
                ('deal_number', models.IntegerField(null=True)),
                ('counterparty', models.CharField(choices=[('Citi', 'Citi'), ('mBank', ' mBank'), ('Societe', 'Societe'), ('Santander', 'Santander')], max_length=30, null=True)),
                ('nominal', models.FloatField(null=True)),
                ('dtm', models.IntegerField(null=True)),
                ('cross', models.CharField(choices=[('EUR/PLN', 'EUR/PLN'), ('USD/PLN', 'USD/PLN'), ('EUR/USD', 'EUR/USD')], max_length=7, null=True)),
                ('exchange_rate', models.FloatField(null=True)),
                ('forward_rate', models.FloatField(null=True)),
                ('result', models.FloatField(null=True)),
                ('iterest', models.FloatField(null=True)),
            ],
        ),
    ]

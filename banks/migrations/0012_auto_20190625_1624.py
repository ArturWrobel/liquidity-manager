# Generated by Django 2.2.2 on 2019-06-25 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0011_auto_20190625_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deals',
            name='counterparty',
            field=models.CharField(choices=[('Citi', 'Citi'), ('mBank', ' mBank'), ('Societe', 'Societe'), ('Santander', 'Santander')], max_length=30, null=True),
        ),
    ]
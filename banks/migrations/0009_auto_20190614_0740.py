# Generated by Django 2.2.2 on 2019-06-14 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0008_auto_20190613_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deals',
            name='counterparty_another',
            field=models.CharField(choices=[('Citi', 'Citi'), ('mBank', ' mBank'), ('Societe', 'Societe'), ('Santander', 'Santander')], max_length=30, null=True),
        ),
    ]

# Generated by Django 2.2.2 on 2019-06-13 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0002_deal_mbank_santander_societe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='deal_kind',
            field=models.CharField(choices=[(1, 'DEPO'), (2, 'TXFR'), (1, 'FX_BUY'), (1, 'FX_SELL')], max_length=20, null=True),
        ),
    ]
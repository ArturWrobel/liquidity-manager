# Generated by Django 2.2.2 on 2019-07-01 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0017_auto_20190701_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='deals',
            name='value_date_expiry',
            field=models.DateField(null=True),
        ),
    ]

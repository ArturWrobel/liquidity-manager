# Generated by Django 2.2.2 on 2019-06-25 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0012_auto_20190625_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deals',
            name='deal_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='deals',
            name='value_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
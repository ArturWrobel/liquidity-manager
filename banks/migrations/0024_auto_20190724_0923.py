# Generated by Django 2.2.2 on 2019-07-24 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0023_auto_20190722_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deals',
            name='entity',
            field=models.CharField(max_length=50, null=True),
        ),
    ]

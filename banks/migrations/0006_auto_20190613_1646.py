# Generated by Django 2.2.2 on 2019-06-13 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0005_auto_20190613_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deals',
            name='deal_number',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
# Generated by Django 2.2.2 on 2019-07-18 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0020_eurcurve_plncurve_usdcurve'),
    ]

    operations = [
        migrations.AddField(
            model_name='deals',
            name='frontoffice',
            field=models.CharField(max_length=10, null=True),
        ),
    ]

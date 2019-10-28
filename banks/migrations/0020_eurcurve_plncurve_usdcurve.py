# Generated by Django 2.2.2 on 2019-07-10 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0019_auto_20190701_1738'),
    ]

    operations = [
        migrations.CreateModel(
            name='EurCurve',
            fields=[
                ('date', models.DateField(primary_key=True, serialize=False)),
                ('m1', models.FloatField(default=0)),
                ('m3', models.FloatField(default=0)),
                ('m6', models.FloatField(default=0)),
                ('y1', models.FloatField(default=0)),
                ('y2', models.FloatField(default=0)),
                ('y3', models.FloatField(default=0)),
                ('y4', models.FloatField(default=0)),
                ('y5', models.FloatField(default=0)),
                ('y6', models.FloatField(default=0)),
                ('y7', models.FloatField(default=0)),
                ('y8', models.FloatField(default=0)),
                ('y9', models.FloatField(default=0)),
                ('y10', models.FloatField(default=0)),
                ('y12', models.FloatField(default=0)),
                ('y15', models.FloatField(default=0)),
                ('y20', models.FloatField(default=0)),
                ('y30', models.FloatField(default=0)),
                ('y50', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PlnCurve',
            fields=[
                ('date', models.DateField(primary_key=True, serialize=False)),
                ('m1', models.FloatField(default=0)),
                ('m3', models.FloatField(default=0)),
                ('m6', models.FloatField(default=0)),
                ('y1', models.FloatField(default=0)),
                ('y2', models.FloatField(default=0)),
                ('y3', models.FloatField(default=0)),
                ('y4', models.FloatField(default=0)),
                ('y5', models.FloatField(default=0)),
                ('y6', models.FloatField(default=0)),
                ('y7', models.FloatField(default=0)),
                ('y8', models.FloatField(default=0)),
                ('y9', models.FloatField(default=0)),
                ('y10', models.FloatField(default=0)),
                ('y12', models.FloatField(default=0)),
                ('y15', models.FloatField(default=0)),
                ('y20', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UsdCurve',
            fields=[
                ('date', models.DateField(primary_key=True, serialize=False)),
                ('m1', models.FloatField(default=0)),
                ('m3', models.FloatField(default=0)),
                ('m6', models.FloatField(default=0)),
                ('y1', models.FloatField(default=0)),
                ('y2', models.FloatField(default=0)),
                ('y3', models.FloatField(default=0)),
                ('y4', models.FloatField(default=0)),
                ('y5', models.FloatField(default=0)),
                ('y6', models.FloatField(default=0)),
                ('y7', models.FloatField(default=0)),
                ('y8', models.FloatField(default=0)),
                ('y9', models.FloatField(default=0)),
                ('y10', models.FloatField(default=0)),
                ('y12', models.FloatField(default=0)),
                ('y15', models.FloatField(default=0)),
                ('y20', models.FloatField(default=0)),
                ('y30', models.FloatField(default=0)),
                ('y50', models.FloatField(default=0)),
            ],
        ),
    ]
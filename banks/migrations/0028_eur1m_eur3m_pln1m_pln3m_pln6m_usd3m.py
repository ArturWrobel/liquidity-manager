# Generated by Django 2.2.2 on 2019-11-26 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0027_books'),
    ]

    operations = [
        migrations.CreateModel(
            name='EUR1M',
            fields=[
                ('date', models.DateField(primary_key=True, serialize=False)),
                ('d1', models.FloatField(default=0)),
                ('m1', models.FloatField(default=0)),
                ('m3', models.FloatField(default=0)),
                ('m6', models.FloatField(default=0)),
                ('m9', models.FloatField(default=0)),
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
            ],
        ),
        migrations.CreateModel(
            name='EUR3M',
            fields=[
                ('date', models.DateField(primary_key=True, serialize=False)),
                ('d1', models.FloatField(default=0)),
                ('m1', models.FloatField(default=0)),
                ('m3', models.FloatField(default=0)),
                ('m6', models.FloatField(default=0)),
                ('m9', models.FloatField(default=0)),
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
            ],
        ),
        migrations.CreateModel(
            name='PLN1M',
            fields=[
                ('date', models.DateField(primary_key=True, serialize=False)),
                ('d1', models.FloatField(default=0)),
                ('m1', models.FloatField(default=0)),
                ('m3', models.FloatField(default=0)),
                ('m6', models.FloatField(default=0)),
                ('m9', models.FloatField(default=0)),
                ('y1', models.FloatField(default=0)),
                ('y2', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PLN3M',
            fields=[
                ('date', models.DateField(primary_key=True, serialize=False)),
                ('d1', models.FloatField(default=0)),
                ('m1', models.FloatField(default=0)),
                ('m3', models.FloatField(default=0)),
                ('m6', models.FloatField(default=0)),
                ('m9', models.FloatField(default=0)),
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
            ],
        ),
        migrations.CreateModel(
            name='PLN6M',
            fields=[
                ('date', models.DateField(primary_key=True, serialize=False)),
                ('d1', models.FloatField(default=0)),
                ('m1', models.FloatField(default=0)),
                ('m3', models.FloatField(default=0)),
                ('m6', models.FloatField(default=0)),
                ('m9', models.FloatField(default=0)),
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
            ],
        ),
        migrations.CreateModel(
            name='USD3M',
            fields=[
                ('date', models.DateField(primary_key=True, serialize=False)),
                ('d1', models.FloatField(default=0)),
                ('m1', models.FloatField(default=0)),
                ('m3', models.FloatField(default=0)),
                ('m6', models.FloatField(default=0)),
                ('m9', models.FloatField(default=0)),
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
            ],
        ),
    ]
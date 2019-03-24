# Generated by Django 2.0 on 2019-03-24 05:35

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0010_auto_20190324_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 3, 24, 11, 5, 55, 262331)),
        ),
        migrations.AlterField(
            model_name='offer',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 3, 24, 11, 5, 55, 277958)),
        ),
        migrations.AlterField(
            model_name='rate',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 3, 24, 11, 5, 55, 277958)),
        ),
        migrations.AlterField(
            model_name='rate',
            name='orderid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.Order'),
        ),
    ]
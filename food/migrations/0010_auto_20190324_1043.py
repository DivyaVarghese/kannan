# Generated by Django 2.0 on 2019-03-24 05:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0009_auto_20190323_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 3, 24, 10, 43, 17, 878473)),
        ),
        migrations.AlterField(
            model_name='offer',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 3, 24, 10, 43, 17, 878473)),
        ),
        migrations.AlterField(
            model_name='rate',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 3, 24, 10, 43, 17, 878473)),
        ),
    ]

# Generated by Django 2.0 on 2019-03-21 11:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_offer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.date(2019, 3, 21)),
        ),
        migrations.AlterField(
            model_name='offer',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.date(2019, 3, 21)),
        ),
    ]
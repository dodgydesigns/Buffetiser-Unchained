# Generated by Django 3.2.5 on 2021-08-24 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buffetiser_main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='investment',
            name='average_cost',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='investment',
            name='live_price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='investment',
            name='percent_profit',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='investment',
            name='profit',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='investment',
            name='total_value',
            field=models.FloatField(default=0),
        ),
    ]

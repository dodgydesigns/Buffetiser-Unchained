# Generated by Django 3.2.6 on 2021-09-01 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Investment',
            fields=[
                ('investment_type', models.CharField(choices=[('Shares', 'Shares'), ('Crypto', 'Crypto')], default='Shares', max_length=20)),
                ('name', models.CharField(default='unnamed', max_length=200)),
                ('symbol', models.CharField(default='none', max_length=5, primary_key=True, serialize=False)),
                ('currency', models.CharField(default='AUD', max_length=5)),
                ('exchange', models.CharField(choices=[('XAMS', 'XAMS'), ('XASX', 'XASX'), ('XBOM', 'XBOM'), ('XBRU', 'XBRU'), ('XFRA', 'XFRA'), ('XHKG', 'XHKG'), ('XJPX', 'XJPX'), ('XKOS', 'XKOS'), ('XLIS', 'XLIS'), ('XLON', 'XLON'), ('XMIL', 'XMIL'), ('XMSM', 'XMSM'), ('XNAS', 'XNAS'), ('XNSE', 'XNSE'), ('XNYS', 'XNYS'), ('XOSL', 'XOSL'), ('XSAU', 'XSAU'), ('XSHE', 'XSHE'), ('XSHG', 'XSHG'), ('XSWX', 'XSWX'), ('XTAI', 'XTAI'), ('XTSE', 'XTSE')], default='XASX', max_length=4)),
                ('platform', models.CharField(choices=[('CMC', 'CMC'), ('LINK', 'LINK'), ('BOARDROOM', 'BOARDROOM'), ('DIRECT', 'DIRECT'), ('IPO', 'IPO')], default='CMC', max_length=255)),
                ('units_held', models.FloatField(default=0)),
                ('total_fees', models.FloatField(default=0)),
                ('average_cost', models.FloatField(default=0)),
                ('total_cost', models.FloatField(default=0)),
                ('live_price', models.FloatField(default=0)),
                ('total_value', models.FloatField(default=0)),
                ('profit', models.FloatField(default=0)),
                ('percent_profit', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('units', models.FloatField()),
                ('price', models.FloatField()),
                ('fee', models.FloatField()),
                ('date', models.DateField()),
                ('investment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buffetiser_main.investment')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('units', models.FloatField()),
                ('price', models.FloatField()),
                ('fee', models.FloatField()),
                ('date', models.DateField()),
                ('investment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buffetiser_main.investment')),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('open', models.FloatField()),
                ('high', models.FloatField()),
                ('low', models.FloatField()),
                ('close', models.FloatField()),
                ('investment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buffetiser_main.investment')),
            ],
        ),
    ]

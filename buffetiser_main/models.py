from django.db import models

from buffetiser_main.python.data_structures import Constants


class Investment(models.Model):
    """
    This represents either Shares or Crypto-currency. There is only one of these, of each type:platform:symbol
    in the system.
    Each one of these however, can have multiple purchases and sales.
    PK: symbol (+ exchange- would like to but can't yet. Don't know how).
    """
    investment_type = models.CharField(choices=Constants.InvestmentType.choices,
                                       max_length=20,
                                       default=Constants.InvestmentType.SHARES)
    name = models.CharField(max_length=200, default='unnamed')
    symbol = models.CharField(max_length=5, default='none', primary_key=True)
    currency = models.CharField(max_length=5, default='AUD')
    exchange = models.CharField(choices=Constants.Exchanges.choices,
                                max_length=4,
                                default=Constants.Exchanges.XASX)
    platform = models.CharField(choices=Constants.Platforms.choices,
                                max_length=255,
                                default=Constants.Platforms.CMC)

    units_held = models.FloatField(default=0)               # float so it can handle shares (int) and crypto (float)
    total_fees = models.FloatField(default=0)               # should only really be dollars/cents.
    average_cost = models.FloatField(default=0)             #
    total_cost = models.FloatField(default=0)               # can be any float
    live_price = models.FloatField(default=0)
    total_value = models.FloatField(default=0)
    profit = models.FloatField(default=0)
    percent_profit = models.FloatField(default=0)


class Purchase(models.Model):
    """
    """

    units = models.FloatField()
    price = models.FloatField()
    fee = models.FloatField()
    date = models.DateField()

    investment = models.ForeignKey(to=Investment, on_delete=models.CASCADE)


class Sale(models.Model):
    """
    """
    units = models.FloatField()
    price = models.FloatField()
    fee = models.FloatField()
    date = models.DateField()

    investment = models.ForeignKey(to=Investment, on_delete=models.CASCADE)


class History(models.Model):
    """
    """
    date = models.DateField()
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()

    investment = models.ForeignKey(to=Investment, on_delete=models.CASCADE)

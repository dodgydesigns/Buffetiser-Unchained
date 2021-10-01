from sqlite3 import Date

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

    unitsHeld = models.FloatField(default=0)               # float so it can handle shares (int) and crypto (float)
    totalFees = models.FloatField(default=0)               # should only really be dollars/cents.
    averageCost = models.FloatField(default=0)
    totalCost = models.FloatField(default=0)
    livePrice = models.FloatField(default=0)
    totalValue = models.FloatField(default=0)
    profit = models.FloatField(default=0)
    percentProfit = models.FloatField(default=0)


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
    date = models.DateField(Date.today())
    open = models.FloatField(default=0)
    high = models.FloatField(default=0)
    low = models.FloatField(default=0)
    close = models.FloatField(default=0)
    adjustedClose = models.FloatField(default=0)
    volume = models.IntegerField(default=0)

    investment = models.ForeignKey(to=Investment, on_delete=models.CASCADE)

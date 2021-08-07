from django.db import models


class Investment(models.Model):
    """
    This represents either Shares or Cryptocurrency. There is only one of these in the system.
    PK: symbol + exchange
    """

    class InvestmentType(models.TextChoices):
        """
        We want enumeration for investment type as there is only a set, finite number of choices.
        """
        SHARES = ('SH', 'Shares')
        CRYPTO = ('CR', 'Crypto')

    investment_type = models.CharField(choices=InvestmentType.choices, max_length=2)
    name = models.CharField(max_length=200)
    currency = models.CharField(max_length=2)
    platform = models.CharField(max_length=20)          # CMC, Link, Boardroom, ComputerShare

    # these might be replaced by Purchase and Sale
    units_held = models.FloatField()                    # float so it can handle shares (int) and crypto (float)
    total_cost = models.FloatField()                    # can be any float for crypto
    total_fees = models.FloatField()                    # should only really be dollars/cents.

    symbol = models.CharField(max_length=5)
    exchange = models.CharField(max_length=5, default='ASX')


class Purchase(models.Model):
    units = models.FloatField()
    price = models.FloatField()
    fee = models.FloatField()
    date = models.DateField()

    investment = models.ForeignKey(to=Investment, on_delete=models.CASCADE)


class Sale(models.Model):
    units = models.FloatField()
    price = models.FloatField()
    fee = models.FloatField()
    date = models.DateField()

    investment = models.ForeignKey(to=Investment, on_delete=models.CASCADE)


class History(models.Model):
    date = models.DateField()
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()

    investment = models.ForeignKey(to=Investment, on_delete=models.CASCADE)

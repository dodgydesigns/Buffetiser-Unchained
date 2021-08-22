from django.db import models


class Investment(models.Model):
    """
    This represents either Shares or Crypto-currency. There is only one of these, of each type:platform:symbol
    in the system.
    Each one of these however, can have multiple purchases and sales.
    PK: symbol (+ exchange- would like to but can't yet. Don't know how).
    """

    units_held = models.FloatField()                    # float so it can handle shares (int) and crypto (float)
    total_cost = models.FloatField()                    # can be any float
    total_fees = models.FloatField()                    # should only really be dollars/cents.


class Purchase(models.Model):

    class InvestmentType(models.TextChoices):
        """
        We want enumeration for investment type as there is only a set, finite number of choices.
        """
        SHARES = ('SH', 'Shares')
        CRYPTO = ('CR', 'Crypto')

    investment_type = models.CharField(choices=InvestmentType.choices,
                                       max_length=20,
                                       default=InvestmentType.SHARES)
    name = models.CharField(max_length=200, default='unnamed')
    symbol = models.CharField(max_length=5, default='none', primary_key=True)
    currency = models.CharField(max_length=5, default='AUD')
    exchange = models.CharField(max_length=5, default='ASX')
    platform = models.CharField(max_length=5, default='CMC')          # CMC, Link, Boardroom, ComputerShare
    units = models.FloatField()
    price = models.FloatField()
    fee = models.FloatField()
    date = models.DateField()

    unique_together = ('symbol', 'exchange')
    # investment = models.ForeignKey(to=Investment, on_delete=models.CASCADE)


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

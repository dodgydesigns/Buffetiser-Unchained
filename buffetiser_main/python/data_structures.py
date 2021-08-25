from django.db import models


class Constants:
    class InvestmentType(models.TextChoices):
        """
        We want enumeration for investment type as there is only a set, finite number of choices.
        """
        SHARES = ('Shares', 'Shares')
        CRYPTO = ('Crypto', 'Crypto')

    class Exchanges(models.TextChoices):
        """
        """
        XAMS = ('XAMS', 'XAMS')
        XASX = ('XASX', 'XASX')
        XBOM = ('XBOM', 'XBOM')
        XBRU = ('XBRU', 'XBRU')
        XFRA = ('XFRA', 'XFRA')
        XHKG = ('XHKG', 'XHKG')
        XJPX = ('XJPX', 'XJPX')
        XKOS = ('XKOS', 'XKOS')
        XLIS = ('XLIS', 'XLIS')
        XLON = ('XLON', 'XLON')
        XMIL = ('XMIL', 'XMIL')
        XMSM = ('XMSM', 'XMSM')
        XNAS = ('XNAS', 'XNAS')
        XNSE = ('XNSE', 'XNSE')
        XNYS = ('XNYS', 'XNYS')
        XOSL = ('XOSL', 'XOSL')
        XSAU = ('XSAU', 'XSAU')
        XSHE = ('XSHE', 'XSHE')
        XSHG = ('XSHG', 'XSHG')
        XSWX = ('XSWX', 'XSWX')
        XTAI = ('XTAI', 'XTAI')
        XTSE = ('XTSE', 'XTSE')

    class Platforms(models.TextChoices):
        """
        """
        CMC = ('CMC', 'CMC')
        LINK = ('LINK', 'LINK')
        BOARDROOM = ('BOARDROOM', 'BOARDROOM')
        DIRECT = ('DIRECT', 'DIRECT')
        IPO = ('IPO', 'IPO')

    class Currencies(models.TextChoices):
        """
        We want enumeration for investment type as there is only a set, finite number of choices.
        """
        AUD = ('AUD', 'AUD')
        USD = ('USD', 'USD')
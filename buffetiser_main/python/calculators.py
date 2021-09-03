import logging

# Create and configure logger
logging.basicConfig(filename="debug.log",
                    # format='%(asctime)s %(message)s',
                    format='---------Calculators---------%(message)s',
                    filemode='w')
# Creating an object
logger = logging.getLogger()
# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)


class Calculators:
    def __init__(self, investmentList):
        self.investmentList = investmentList

    def totalCost(self):
        totalCost = 0
        for investment in self.investmentList:
            for purchase in investment.purchase_set.all():
                totalCost += purchase.units * purchase.price
                totalCost += purchase.fee
        return totalCost

    def totalValue(self):
        totalValue = 0
        for investment in self.investmentList:
            totalValue += investment.units_held * investment.live_price
            logger.debug(investment.units_held, investment.live_price)
        return totalValue

    def dayValue(self):
        pass

    def totalProfit(self):
        return self.totalValue() - self.totalCost()

    def totalProfitPercent(self):
        if self.totalCost() > 0:
            return ((self.totalValue() - self.totalCost()) / self.totalCost()) * 100
        else:
            return 0


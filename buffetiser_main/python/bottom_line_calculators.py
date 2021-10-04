import logging

# Create and configure logger
logging.basicConfig(filename="debug.log",
                    # format='%(asctime)s %(message)s',
                    format='---------BottomLineCalculators---------%(message)s',
                    filemode='w')
# Creating an object
logger = logging.getLogger()
# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)


class BottomLineCalculators:
    """
    Get the total portfolio values.
    """
    def __init__(self, investmentList):
        self.investmentList = investmentList

    def bottomLineCost(self):
        totalCost = 0
        for investment in self.investmentList:
            for purchase in investment.purchase_set.all():
                totalCost += purchase.units * purchase.price
                totalCost += purchase.fee
        return totalCost

    def bottomLineValue(self):
        totalValue = 0
        for investment in self.investmentList:
            totalValue += investment.unitsHeld * investment.livePrice
        return totalValue

    def dayValue(self):
        pass

    def bottomLineProfit(self):
        return self.bottomLineValue() - self.bottomLineCost()

    def bottomLineProfitPercent(self):
        if self.bottomLineCost() > 0:
            return (self.bottomLineProfit() / self.bottomLineCost()) * 100
        else:
            return 100


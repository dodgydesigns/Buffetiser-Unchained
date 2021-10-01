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


class IndividualInvestmentCalculators:
    def __init__(self, investment):
        self.investment = investment

    def assignTotalCost(self):
        totalCost = 0
        for purchase in self.investment.purchase_set.all():
            totalCost += purchase.units * purchase.price
            totalCost += purchase.fee
        self.investment.totalCost = totalCost

    def assignTotalValue(self):
        totalValue = 0
        self.investment.totalValue = self.investment.unitsHeld * self.investment.livePrice
        logger.debug("held " + str(self.investment.unitsHeld) + " " + str(self.investment.livePrice) + " " +
                     str(self.investment.totalValue))
        return totalValue

    def assignDayValue(self):
        pass

    def assignTotalProfit(self):
        self.investment.profit = self.investment.totalValue - self.investment.totalCost

    def assignTotalProfitPercent(self):
        if self.investment.totalCost > 0:
            self.investment.percentProfit = ((self.investment.totalValue - self.investment.totalCost) /
                                             self.investment.totalCost) * 100
        else:
            return 100.0

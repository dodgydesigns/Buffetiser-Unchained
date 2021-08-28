

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
        return totalValue

    def dayValue(self):
        pass

    def totalProfit(self):
        return self.totalValue() - self.totalCost()

    def totalProfitPercent(self):
        return ((self.totalValue() - self.totalCost()) / self.totalCost()) * 100

    # def averageCost(self, symbol):
    #
    #     totalCost = 0
    #     for investment in self.investmentList:
    #         for purchase in investment.purchase_set.all():
    #             totalCost += purchase.units * purchase.price
    #             totalCost += purchase.fee
    #     return totalCost / len(investment.purchase_set.all())
    #
    # def totalCost(self, symbol):
    #
    #     totalCost = 0
    #     for purchase in self.investmentList.get(symbol).purchase_set.all():
    #         totalCost += purchase.units * purchase.price
    #         totalCost += purchase.fee
    #     return totalCost

from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from buffetiser_main.models import Purchase, Investment, History
from .python.data_structures import Constants
from .python.individual_investment_calculators import IndividualInvestmentCalculators
from .python.network import useBigCharts
from .python.bottom_line_calculators import BottomLineCalculators

import logging

# Create and configure logger
from .python.plots import plotPriceHistory

logging.basicConfig(filename="debug.log",
                    # format='%(asctime)s %(message)s',
                    format='----------Views--------%(message)s',
                    filemode='w')
# Creating an object
logger = logging.getLogger()
# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)


def main(request):
    """

    """
    investment_list = Investment.objects.order_by('symbol')  # [:5] #if investment_list else []
    # calculate totals for all investments
    calculator = BottomLineCalculators(investment_list)
    bottomLineCost = calculator.bottomLineCost()
    bottomLineValue = calculator.bottomLineValue()
    bottomLineProfit = calculator.bottomLineProfit()
    bottomLineProfitPercent = calculator.bottomLineProfitPercent()

    context = {'investment_list': investment_list,
               'bottom_line_cost': bottomLineCost,
               'bottom_line_value': bottomLineValue,
               'bottom_line_profit': bottomLineProfit,
               'bottom_line_profit_percent': bottomLineProfitPercent}

    return render(request, 'buffetiser_main/index.html', context)


def config(request):
    text = "<h1>Buffetiser Unchained Config!</h1>"
    return HttpResponse(text)


def buffetiserHelp(request):
    text = "<h1>Buffetiser Unchained Help!</h1>"
    return HttpResponse(text)


def investmentDetails(request, symbol):
    investment = get_object_or_404(Investment, pk=symbol)
    return render(request, 'buffetiser_main/investment_details.html', {'investment': investment})


def newPurchase(request):
    constants = Constants()
    investment_list = [Investment.objects.all()]
    context = {'constants': constants,
               'investment_list': investment_list}
    return render(request, 'buffetiser_main/new_purchase.html', context)


def addPurchase(request):
    """
    Add a new record of an investment purchase.
    """
    today = datetime.today()
    todayString = '{}-{}-{}'.format(today.year, today.month, today.strftime("%d"))

    # Pull data entered into Purchase form
    investment_type = request.POST.get('type', '---')
    symbol = request.POST.get('symbol', '---')
    name = request.POST.get('name', '---')
    exchange = request.POST.get('exchange', '---')
    platform = request.POST.get('platform', '---')
    currency = request.POST.get('currency', '---')
    units = int(request.POST.get('units', '---'))
    price = float(request.POST.get('price', '---'))
    fee = float(request.POST.get('fee', '---'))
    date = request.POST.get('date', '---')

    # If the investment (symbol) already exists, append additional data. Otherwise, create a new Investment.
    investment, investmentCreated = Investment.objects.get_or_create(symbol=symbol)

    # If it's a new Investment, start adding basic data.
    if investmentCreated:
        investment.investment_type = investment_type
        investment.name = name
        investment.exchange = exchange
        investment.platform = platform
        investment.currency = currency

    # If it's new or existing Investment, add details of the new Purchase.
    unitsHeld = int(units) + investment.unitsHeld
    totalFees = float(fee) + investment.totalFees
    totalCost = float((unitsHeld * price) + totalFees) + investment.totalCost
    averageCost = float(totalCost / unitsHeld)

    # Now we need the live price so we can calculate the final fields.
    getInvestmentData('useBigCharts', investment, todayString)

    totalValue = float((unitsHeld * investment.livePrice))
    profit = float((totalValue - totalCost))
    percentProfit = float((profit / totalCost) * 100)

    # Add all the new data to the Investment object and save to DB.
    investment.unitsHeld = unitsHeld
    investment.totalFees = totalFees
    investment.totalCost = totalCost
    investment.averageCost = averageCost
    investment.totalValue = totalValue
    investment.profit = profit
    investment.percentProfit = percentProfit
    investment.save()

    purchase = Purchase(units=units,
                        price=price,
                        fee=fee,
                        date=date,
                        investment=investment)

    purchase.save()

    return redirect('/')


def updateLivePrices(request):
    """
    Update the day values for each investment
    """
    # TODO: this should only happen once a day to stop us from hammering the service provider
    today = datetime.today()
    todayString = '{}-{}-{}'.format(today.year, today.month, today.strftime("%d"))

    for investment in Investment.objects.all():
        getInvestmentData('useBigCharts', investment, todayString)

    return redirect('/')


def getInvestmentData(service, investment, todayString):
    """

    """
    if service == 'useBigCharts':
        investmentData = useBigCharts(investment.symbol, todayString)

    historyObject = History(date=investmentData.get('date'),
                            open=investmentData.get('open'),
                            high=investmentData.get('high'),
                            low=investmentData.get('low'),
                            close=investmentData.get('close'),
                            adjustedClose=investmentData.get('adjustedClose'),
                            volume=investmentData.get('volume'),
                            investment=investment)

    historyObject.save()

    # TODO: does this have to be done???
    investment.livePrice = investmentData.get('close')
    calculator = IndividualInvestmentCalculators(investment)
    calculator.assignDayValue()
    calculator.assignTotalCost()
    calculator.assignTotalValue()
    calculator.assignTotalProfit()
    calculator.assignTotalProfitPercent()

    # add plot path
    investment.plotPath = plotPriceHistory(investment)

    investment.save()

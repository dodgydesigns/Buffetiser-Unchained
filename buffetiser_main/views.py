from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from buffetiser_main.models import Purchase, Investment
from .python.data_structures import Constants
from .python.network import useBigCharts
from .python.calculators import Calculators

import logging

# Create and configure logger
logging.basicConfig(filename="debug.log",
                    # format='%(asctime)s %(message)s',
                    format='------------------%(message)s',
                    filemode='w')
# Creating an object
logger = logging.getLogger()
# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)


def main(request, investment_list=None):
    """

    """
    investment_list = Investment.objects.order_by('symbol')  # [:5] #if investment_list else []

    # Update the day values for each investment
    # TODO: this should only happen once a day to stop us from hammering the service provider
    for investment in investment_list:
        historyObject = useBigCharts(investment)
        # historyObject,
        investment.live_price = float(historyObject.close)
        historyObject.save()

    # calculate totals
    calculator = Calculators(investment_list)
    totalCost = calculator.totalCost()
    totalValue = calculator.totalValue()
    totalProfit = calculator.totalProfit()
    totalProfitPercent = calculator.totalProfitPercent()
    context = {'investment_list': investment_list,
               'total_cost': totalCost,
               'total_value': totalValue,
               'total_profit': totalProfit,
               'total_profit_percent': totalProfitPercent}
    return render(request, 'buffetiser_main/index.html', context)


def config(request):
    text = "<h1>Buffetiser Unchained Config!</h1>"
    return HttpResponse(text)


def help(request):
    text = "<h1>Buffetiser Unchained Help!</h1>"
    return HttpResponse(text)


def investmentDetails(request, symbol):
    investment = get_object_or_404(Investment, pk=symbol)
    return render(request, 'buffetiser_main/investment_details.html', {'investment': investment})


def newPurchase(request):
    logger.debug("newPurchase logging started")
    constants = Constants()
    investment_list = Investment.objects.all()
    context = {'constants': constants,
               'investment_list': investment_list}
    return render(request, 'buffetiser_main/new_purchase.html', context)


def addPurchase(request):

    type = request.POST.get('type', '---')
    symbol = request.POST.get('symbol', '---')
    name = request.POST.get('name', '---')
    exchange = request.POST.get('exchange', '---')
    platform = request.POST.get('platform', '---')
    currency = request.POST.get('currency', '---')
    units = int(request.POST.get('units', '---'))
    price = float(request.POST.get('price', '---'))
    fee = float(request.POST.get('fee', '---'))
    date = request.POST.get('date', '---')

    investment, investmentCreated = Investment.objects.get_or_create(symbol=symbol)

    if investmentCreated:
        investment.investment_type = type
        investment.name = name
        investment.exchange = exchange
        investment.platform = platform
        investment.currency = currency

    investment.units_held += int(units)
    investment.total_fees += float(fee)
    investment.total_cost += float((units * price) + fee)
    investment.average_cost = float(investment.total_cost / investment.units_held)
    investment.total_value = float((investment.units_held * investment.live_price))
    investment.profit = float((investment.total_value - investment.total_cost))
    investment.percent_profit += float((investment.profit / investment.total_cost) * 100)

    purchase = Purchase(units=units,
                        price=price,
                        fee=fee,
                        date=date,
                        investment=investment)

    historyObject = useBigCharts(investment)
    investment.live_price = float(historyObject.close)
    historyObject.save(investment=investment)

    investment.save()
    purchase.save()
    historyObject.save()

    logger.debug("Added purchase:  %s %s %s %s %s %s %s %s %s %s".format(type, symbol, name, exchange,
                                                                         platform, currency, units, price, fee, date))
    return redirect('/')

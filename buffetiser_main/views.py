from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from buffetiser_main.models import Purchase, Investment
from .python.calculators import Calculators
from .python.network import useBigCharts


def main(request, investment_list=None):
    """

    """

    investment_list = Investment.objects.order_by('symbol')#[:5] #if investment_list else []
    calculators = Calculators(investment_list)

    context = {'investment_list': investment_list}
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
    emptyPurchase = Purchase()
    return render(request, 'buffetiser_main/new_purchase.html', {'emptyPurchase': emptyPurchase})


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

    investment, investmentCreated = Investment.objects.get_or_create(symbol=symbol,
                                                                     investment_type=type,
                                                                     name=name,
                                                                     exchange=exchange,
                                                                     platform=platform,
                                                                     currency=currency)
    investment.units_held += int(units)
    investment.total_fees += float(fee)
    investment.total_cost += float((units * price) + fee)
    investment.average_cost = float(investment.total_cost / investment.units_held)
    investment.live_price = float(useBigCharts(symbol).get("close"))
    investment.total_value = float((investment.units_held * investment.live_price))
    investment.profit = float((investment.total_value - investment.total_cost))
    investment.percent_profit += float((investment.profit / investment.total_cost) * 100)

    purchase = Purchase(units=units,
                        price=price,
                        fee=fee,
                        date=date,
                        investment=investment)

    investment.save()
    purchase.save()

    # response = "Added purchase:  %s %s %s %s %s %s %s %s %s %s"
    # return HttpResponse(response % (type, symbol, name, exchange, platform, currency, units, price, fee, date))
    return redirect('/')

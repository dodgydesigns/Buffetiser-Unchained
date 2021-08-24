from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from buffetiser_main.models import Purchase


def main(request):

    investment_list = Purchase.objects.order_by('-date')[:5]
    context = {'investment_list': investment_list}
    return render(request, 'buffetiser_main/index.html', context)


def config(request):
    text = "<h1>Buffetiser Unchained Config!</h1>"
    return HttpResponse(text)


def help(request):
    text = "<h1>Buffetiser Unchained Help!</h1>"
    return HttpResponse(text)


def investmentDetails(request, symbol):
    investment = get_object_or_404(Purchase, pk=symbol)
    return render(request, 'buffetiser_main/investment_details.html', {'investment': investment})


def newPurchase(request):
    emptyPurchase = Purchase()
    return render(request, 'buffetiser_main/new_purchase.html', {'emptyPurchase': emptyPurchase})


def addPurchase(request):

    type = request.POST.get('type', '---')
    symbol = request.POST['symbol']
    name = request.POST['name']
    exchange = request.POST.get('exchange', '---')
    platform = request.POST.get('platform', '---')
    currency = request.POST.get('currency', '---')
    units = request.POST['units']
    price = request.POST['price']
    fee = request.POST['fee']
    date = request.POST['date']

    purchase = Purchase(investment_type=type,
                        symbol=symbol,
                        name=name,
                        exchange=exchange,
                        platform=platform,
                        currency=currency,
                        units=units,
                        price=price,
                        fee=fee,
                        date=date)
    purchase.save()
    response = "Added purchase:  %s %s %s %s %s %s %s %s %s %s"
    return HttpResponse(response % (type, symbol, name, exchange, platform, currency, units, price, fee, date))

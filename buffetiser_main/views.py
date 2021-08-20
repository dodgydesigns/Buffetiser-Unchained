from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from buffetiser_main.models import Investment, Purchase


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
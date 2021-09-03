import logging
from datetime import datetime
import requests
from bs4 import BeautifulSoup

from buffetiser_main.models import History, Investment

# Create and configure logger
logging.basicConfig(filename="debug.log",
                    # format='%(asctime)s %(message)s',
                    format='------------------%(message)s',
                    filemode='w')
# Creating an object
logger = logging.getLogger()
# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)


def useBigCharts(investment):
    """
    Uses ASX data from BigCharts (MarketWatch) to propagate portfolio with share data.
    There is no official API so data is scraped from their website. Not sure if this breaks terms of use.
    :param symbol: The investment to fetch data for.
    """
    today = datetime.today()
    todayString = '{}-{}-{}'.format(today.year, today.month, today.strftime("%d"))

    url = 'https://bigcharts.marketwatch.com/quotes/multi.asp?view=q&msymb=' + \
          'au:{}+'.format(investment.symbol)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    lastPrice = soup.find('td', {'class': 'last-col'}).text
    high = soup.find('td', {'class': 'high-col'}).text
    low = soup.find('td', {'class': 'low-col'}).text
    volume = soup.find('td', {'class': 'volume-col'}).text

    historyObject = History(date=todayString,
                            open=float(low),
                            high=float(high),
                            low=float(low),
                            close=float(lastPrice),
                            adjustedClose=float(lastPrice),
                            volume=int(volume.replace(',', '')),
                            investment=investment)

    return historyObject

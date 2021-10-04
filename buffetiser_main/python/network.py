import logging
import requests
from bs4 import BeautifulSoup

from buffetiser_main.models import History

# Create and configure logger
logging.basicConfig(filename="debug.log",
                    # format='%(asctime)s %(message)s',
                    format='--------useBigCharts----------%(message)s',
                    filemode='w')
# Creating an object
logger = logging.getLogger()
# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)


def useBigCharts(symbol, todayString):
    """
    Uses ASX data from BigCharts (MarketWatch) to propagate portfolio with share data.
    There is no official API so data is scraped from their website. Not sure if this breaks terms of use.
    :param symbol: The investment symbol to fetch data for.
    :param todayString: The date for today.
    """

    url = 'https://bigcharts.marketwatch.com/quotes/multi.asp?view=q&msymb=' + \
          'au:{}+'.format(symbol)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    lastPrice = soup.find('td', {'class': 'last-col'}).text
    high = soup.find('td', {'class': 'high-col'}).text
    low = soup.find('td', {'class': 'low-col'}).text
    volume = soup.find('td', {'class': 'volume-col'}).text

    investmentData = {'date': todayString,
                      'open': float(low),
                      'high': float(high),
                      'low': float(low),
                      'close': float(lastPrice),
                      'adjustedClose': float(lastPrice),
                      'volume': int(volume.replace(',', ''))}

    return investmentData

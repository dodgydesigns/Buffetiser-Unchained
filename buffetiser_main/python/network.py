from datetime import datetime
import requests
from bs4 import BeautifulSoup


def useBigCharts(symbol):
    """
    Uses ASX data from BigCharts (MarketWatch) to propagate portfolio with share data.
    There is no official API so data is scraped fro website. Not sure if this breaks terms of use.
    :param symbol: The investment to fetch data for.
    """
    today = datetime.today()
    todayString = '{}-{}-{}'.format(today.year, today.month, today.strftime("%d"))

    url = 'https://bigcharts.marketwatch.com/quotes/multi.asp?view=q&msymb=' + \
          'au:{}+'.format(symbol)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    lastPrice = soup.find('td', {'class': 'last-col'}).text
    high = soup.find('td', {'class': 'high-col'}).text
    low = soup.find('td', {'class': 'low-col'}).text
    volume = soup.find('td', {'class': 'volume-col'}).text

    currentPriceObject = {"date": todayString,
                          "open": float(low),
                          "high": float(high),
                          "low": float(low),
                          "close": float(lastPrice),
                          "adjusted_close": float(lastPrice),
                          "volume": int(volume.replace(',', ''))}

    return currentPriceObject

import logging
import os
from pathlib import Path

import pygal

# Create and configure logger
from buffetiser_main.models import History

logging.basicConfig(filename="debug.log",
                    # format='%(asctime)s %(message)s',
                    format='---------Plots---------%(message)s',
                    filemode='w')
# Creating an object
logger = logging.getLogger()
# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

INVESTMENT_PLOT_STYLE = pygal.style.DarkStyle
TOTALS_PLOT_STYLE = pygal.style.DarkStyle

# This is where the data directory will be located. Should be in user's home.
DATA_PATH = str(os.path.join(Path.home(), 'buffetiser'))


def plotPriceHistory(investment):

    history = History.objects.filter(investment=investment)
    maxValue = max([float(value.close) for value in history])

    investmentPlot = pygal.Line(width=1000,
                                height=300,
                                dots_size=0.75,
                                max_scale=maxValue,
                                legend_box_size=5,
                                show_y_guides=False,
                                y_labels_major_every=2,
                                show_minor_y_labels=False,
                                human_readable=True,
                                x_label_rotation=30,
                                tooltip_border_radius=10,
                                show_minor_x_labels=False,
                                style=INVESTMENT_PLOT_STYLE)

    investmentPlot.title = '{} ({})'.format(investment.name, investment.symbol)
    dateList = []
    lowList = []
    highList = []
    closeList = []
    for entry in history:
        dateList.append('{}-{}-{}'.format(entry.date.year, entry.date.month, entry.date.day))
        # TODO: better way to do this?
        lowList.append(entry.low)
        highList.append(entry.high)
        closeList.append(entry.close)

    investmentPlot.x_labels = dateList
    # TODO: figure a good algorithm to determine the best number of x-axis entries
    investmentPlot.x_labels_major = dateList[::2]
    investmentPlot.add('Low', lowList)
    investmentPlot.add('High', highList)
    investmentPlot.add('Close', closeList)
    # TODO: get path properly - HTML can use static to get absolute path to img.
    path = os.path.join('/Users/mullsy/workspace/Buffetiser_Unchained/buffetiser_main/static/buffetiser_main/img/',
                        investment.symbol + '.svg')
    investmentPlot.render_to_file(path)

    return 'buffetiser_main/img/' + investment.symbol + '.svg'

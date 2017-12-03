import matplotlib
import json
matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np

with open('data.json', 'r') as f:
    json_str = f.read()
    percent = json.loads(json_str)

for coin in percent:
    base = percent[coin][0]
    for i in range(13):
        if (base != 0):
            percent[coin][i] = ((percent[coin][i] / base) - 1) * 100

with open('percentages.json', 'w') as f:
    json.dump(percent, f)

for coin in percent:
    # Data for plotting
    t = np.arange(0, 65, 5)
    p = np.array(percent[coin])

    # Note that using plt.subplots below is equivalent to using
    # fig = plt.figure and then ax = fig.add_subplot(111)
    fig, ax = plt.subplots()
    ax.plot(t, p)

    ax.set(xlabel='time (min)', ylabel='percent change',
        title='Percent Change of {0} Over 60 Minutes'.format(coin.title()))
    ax.grid()
    fig.savefig("/home/Alex/coins/new/graphs/{0}.png".format(coin), bbox_inches='tight')
    plt.show()
    plt.close()

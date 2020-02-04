import matplotlib.pyplot as plt
import random
import time
import json
import datetime as datetime
import calendar
import time
import numpy as np
totalRp = 0
newDictionary = {}
with open('rpPurchases.json') as json_file:
    purchases = json.load(json_file)

for i in purchases:
    totalRp = totalRp + i['amount']
    date = time.strftime("%a, %d %b %Y %H:%M:%S +0000",
                         time.localtime(i['created']/1000))
    datetime_object = datetime.datetime.strptime(
        date, '%a, %d %b %Y %H:%M:%S +0000')
    newDictionary.update({i['id']: {
        'date': date,
        'datetime': datetime_object,
        'epoch': i['created'],
        'amount': i['amount']}})


# with open('rpPurchases v2.json', 'w') as outfile:
#     json.dump(newDictionary, outfile)
x = []
y = []
for i in newDictionary.items():
    # print(i[1]['datetime'])
    x.append(i[1]['datetime'])
    y.append(i[1]['amount'])
# make up some data
# x = [datetime.datetime.now() + datetime.timedelta(hours=i) for i in range(12)]
# y = [i+random.gauss(0, 1) for i, _ in enumerate(x)]

# plot

plt.plot(x, y)
# beautify the x-labels
plt.gcf().autofmt_xdate()

plt.show()

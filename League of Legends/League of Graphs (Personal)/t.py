import numpy as np
import json
import pandas as pd
import matplotlib.pyplot as plt

plt.rcdefaults()

with open('best.json') as json_file:
    data = json.load(json_file)

print(data.keys())
keyz = []
champs = []
for i in data.keys():
    champs = []
    names = []
    for z in data[i]:
        champs.append(z['value'])
        names.append(z['name'])
    index = np.arange(len(names))
    plt.figure(figsize=(15, 6))
    plt.plot(index, champs)     # Line graph:
    # plt.bar(index, champs)      # Bar graph:
    plt.xlabel('Champions', fontsize=5)
    plt.ylabel('Numder', fontsize=5)
    plt.xticks(index, names, fontsize=5, rotation=90)
    if champs[len(champs)-1] == 0:
        plt.ylim(champs[len(champs)-1], champs[0]+1)
    else:
        plt.ylim(champs[len(champs)-1]-.25, champs[0]+.25)
    plt.title(i)
    # plt.show()
    # print(plt.rcParams["figure.figsize"] )

    plt.savefig("./line/"+i+'.png')
    # break

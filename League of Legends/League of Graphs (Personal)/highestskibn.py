import cassiopeia as cass
import random
import urllib
import json
API_KEY = 'RGAPI-020d0dfd-fb60-45b9-ad97-e636232d6e2c'
CHAMPION_URL = 'https://ddragon.leagueoflegends.com/cdn/9.14.1/data/en_US/championFull.json'
OPEN_JSON = "skins.json"


# This overrides the value set in your configuration/settings.
cass.set_riot_api_key(API_KEY)
cass.set_default_region("NA")

with open(OPEN_JSON) as json_file:
    data = json.load(json_file)


class champ:
    amount = 0
    name = ''

    def __init__(self, n, a):
        self.amount = a
        self.name = n


champs = []
for i in data.items():
    # for y in i[1][0]:
        # print(y)
    champs.append(champ(str(i[0]), len(i[1][0])))
    # print("Name: " + str(i[0])+", Amount:" + str(len(i[1][0])))

champs.sort(key = lambda c: c.amount) #about 9 - 6.1 = 3 secs

for i in champs:
    print(i.name,": ",i.amount)

import cassiopeia as cass
import random
import urllib
import json
API_KEY = 'RGAPI-020d0dfd-fb60-45b9-ad97-e636232d6e2c'
CHAMPION_URL = 'https://ddragon.leagueoflegends.com/cdn/9.14.1/data/en_US/championFull.json'
OPEN_JSON = "stats.json"


# This overrides the value set in your configuration/settings.
cass.set_riot_api_key(API_KEY)
cass.set_default_region("NA")

with open(OPEN_JSON) as json_file:
    data = json.load(json_file)

champions = []


class champ:
    hp = 0
    hpperlevel = 0
    mp = 0
    mpperlevel = 0
    movespeed = 0
    armor = 0
    armorperlevel = 0
    spellblock = 0
    spellblockperlevel = 0
    attackrange = 0
    hpregen = 0
    hpregenperlevel = 0
    mpregen = 0
    mpregenperlevel = 0
    crit = 0
    critperlevel = 0
    attackdamage = 0
    attackdamageperlevel = 0
    attackspeedperlevel = 0
    attackspeed = 0
    name = ''
    att_dict = {}

    def __init__(self, *args):
        # print(args)
        self.name = args[0]
        self.att_dict = args[1][0]
        self.hp = args[1][0]['hp']
        self.hpperlevel = args[1][0]['hpperlevel']
        self.mp = args[1][0]['mp']
        self.mpperlevel = args[1][0]['mpperlevel']
        self.movespeed = args[1][0]['movespeed']
        self.armor = args[1][0]['armor']
        self.armorperlevel = args[1][0]['armorperlevel']
        self.spellblock = args[1][0]['spellblock']
        self.spellblockperlevel = args[1][0]['spellblockperlevel']
        self.attackrange = args[1][0]['attackrange']
        self.hpregen = args[1][0]['hpregen']
        self.hpregenperlevel = args[1][0]['hpregenperlevel']
        self.mpregen = args[1][0]['mpregen']
        self.mpregenperlevel = args[1][0]['mpregenperlevel']
        self.crit = args[1][0]['crit']
        self.critperlevel = args[1][0]['critperlevel']
        self.attackdamage = args[1][0]['attackdamage']
        self.attackdamageperlevel = args[1][0]['attackdamageperlevel']
        self.attackspeedperlevel = args[1][0]['attackspeedperlevel']
        self.attackspeed = args[1][0]['attackspeed']

    def getattr(self, x):
        return self.att_dict[x]


for i in data.items():
    champions.append(champ(i[0], i[1]))

data2 = {}

for i in data.items():
    for k in i[1][0].keys():
        champions.sort(key=lambda c: c.getattr(k))
        champions.reverse()
        data2[k] = []
# :int(len(champions)/2)
        for i in champions:
            data2[k].append({'name': i.name,
                             'value': i.getattr(k)})

    break


# champions.sort(key=lambda c: c.attackdamage)
# champions.reverse()
# for i in champions[:10]:
#     print(i.name, " : ", i.attackdamage)

with open('best.json', 'w') as outfile:
    json.dump(data2, outfile)

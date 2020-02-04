import random
import urllib
import json
import urllib.request
import urllib.parse
import numpy as np
import pandas as pd
from os import path
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import operator
import time
import datetime
import matplotlib

class LeagueProfile():
    RiotApiKey = "RGAPI-5cb32e57-c3e9-4712-be4f-eb09c9f71a49"
    ProfileData = {}

    SummonerName = ""
    SummonerNameUrl = ''
    MatchHistory = {}

    def __init__(self, name):
        self.SummonerName = name
        self.SummonerNameUrl = urllib.parse.quote(name)
        self.getProfleByName()

    def getProfleByName(self):
        with urllib.request.urlopen("https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" +
                                    self.SummonerNameUrl + "?api_key=" + self.RiotApiKey) as url:
            self.ProfileData = json.loads(url.read().decode())
            return self.ProfileData

    def getChampionMasteryScoreBySummonerId(self):
        with urllib.request.urlopen("https://na1.api.riotgames.com/lol/champion-mastery/v4/scores/by-summoner/" +
                                    self.ProfileData['id'] + "?api_key=" + self.RiotApiKey) as url:
            return json.loads(url.read().decode())

    def getChampionMasteriesBySummonerId(self):
        with urllib.request.urlopen("https://na1.api.riotgames.com//lol/champion-mastery/v4/champion-masteries/by-summoner/" +
                                    self.ProfileData['id'] + "?api_key=" + self.RiotApiKey) as url:
            return json.loads(url.read().decode())

    def getRecentGames(self):
        with urllib.request.urlopen("https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/" +
                                    self.ProfileData['accountId'] + "?api_key=" + self.RiotApiKey) as url:
            self.match_history = json.loads(url.read().decode())
            return self.match_history['matches']

    def randomColor(self, word, font_size, position, orientation, random_state=None,
                    **kwargs):
        import random
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        rgb2 = [r, g, b]
        return tuple(rgb2)

    def getOldestPlayedChampions(self):
        championDict = self.getChampionMasteriesBySummonerId()

        newDict = {}
        newarr = []
        with open('./ChampionKeys.json', encoding="utf8") as json_file:
            keys = json.load(json_file)

        for i in championDict:
            name = list(keys.keys())[
                list(keys.values()).index(i['championId'])]

            date = time.strftime("%a, %d %b %Y %H:%M:%S +0000",
                                 time.localtime(i['lastPlayTime']/1000))
            datetime_object = datetime.datetime.strptime(
                date, '%a, %d %b %Y %H:%M:%S +0000')

            newarr.append({'name': name, 'masteryPoints': i['championPoints'], 'lastDate':
                           str(datetime_object), 'datev2': date, 'epoch': i['lastPlayTime']})
        newarr = sorted(newarr, key=lambda i: i['epoch'])
        x = []
        xlabels=[]
        y = []
        for i in newarr:
            # print(i[1]['datetime'])
            x.append(i['lastDate'])
            xlabels.append(str(i['lastDate'])[0:10])
            y.append(i['name'])
        # make up some data
        # x = [datetime.datetime.now() + datetime.timedelta(hours=i) for i in range(12)]
        # y = [i+random.gauss(0, 1) for i, _ in enumerate(x)]

        # plot

        plt.plot(x, y)
        
        plt.xticks(x,xlabels,rotation=75)
        # beautify the x-label
        fig = matplotlib.pyplot.gcf()
        fig.set_size_inches(40, 35)
        plt.savefig('./'+lp.SummonerName+'-oldest.png')

        # with open('./'+lp.SummonerName+'-oldest.json', 'w') as outfile:
        #     json.dump(x, outfile)

        return newarr

    def getRecentGamesPlayedWordCloud(self):
        keys = {}
        with open('./ChampionKeys.json', encoding="utf8") as json_file:
            keys = json.load(json_file)
        lp = LeagueProfile('BIG SQUEEZER')

        x = lp.getRecentGames()
        recentChamps = ""

        for i in self.getRecentGames():
            name = list(keys.keys())[list(keys.values()).index(i['champion'])]
            recentChamps = recentChamps + " " + name
        wordcloud = WordCloud(color_func=self.randomColor,
                              width=1920, height=1080).generate(recentChamps)

        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        # plt.show()
        plt.savefig(self.SummonerName+'.png')


if __name__ == "__main__":
    lp = LeagueProfile('kinky kev')
    x = lp.getOldestPlayedChampions()

    # lp.getRecentGamesPlayedWordCloud()

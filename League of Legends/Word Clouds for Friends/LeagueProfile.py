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
    RiotApiKey = ''
    ProfileData = {}
    SummonerName = ""
    SummonerNameUrl = ''
    MatchHistory = {}

    def __init__(self, riot_api_key, name):
        self.RiotApiKey = riot_api_key
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
        arr2 = championDict
        with open('./OldestChamps/'+lp.SummonerName+'-Mstry.json', 'w') as outfile:
            json.dump(arr2, outfile)
        newDict = {}
        newarr = []
        with open('./ChampionKeys.json', encoding="utf8") as json_file:
            keys = json.load(json_file)

        for i in championDict:
            # Get champion from list
            name = list(keys.keys())[
                list(keys.values()).index(i['championId'])]
            # Dates
            date = time.strftime("%a, %d %b %Y %H:%M:%S +0000",
                                 time.localtime(i['lastPlayTime']/1000))

            datetime_object = datetime.datetime.strptime(
                date, '%a, %d %b %Y %H:%M:%S +0000')
            # Add dictionary objec to array for comparison later
            newarr.append({'name': name, 'masteryPoints': i['championPoints'], 'lastDate':
                           str(datetime_object), 'datev2': date, 'epoch': i['lastPlayTime']})
        newarr = sorted(newarr, key=lambda i: i['epoch'])
        x = []
        xlabels = []
        y = []
        # Set axis data and x labels because the datetime strings are too long
        for i in newarr[:10]:
            x.append(i['lastDate'])
            xlabels.append(str(i['lastDate'])[0:10])
            y.append(i['name'])

        # make up some data
        # x = [datetime.datetime.now() + datetime.timedelta(hours=i) for i in range(12)]
        # y = [i+random.gauss(0, 1) for i, _ in enumerate(x)]

        # plot
        plt.plot(x, y)

        # Rotate dates because they dont fit too well
        plt.xticks(x, xlabels, rotation=35)

        # beautify the x-label
        fig = matplotlib.pyplot.gcf()

        # Resize figure
        fig.set_size_inches(15, 8)

        # Save Image to Folder
        plt.savefig('./OldestChamps/'+lp.SummonerName+'-oldest.png')

        # Save JSON data to folder
        arr2 = newarr
        with open('./OldestChamps/'+lp.SummonerName+'-oldest.json', 'w') as outfile:
            json.dump(arr2, outfile)

        return newarr

    def getRecentGamesPlayedWordCloud(self):
        keys = {}
        with open('./ChampionKeys.json', encoding="utf8") as json_file:
            keys = json.load(json_file)
        recentChamps = ""

        for i in self.getRecentGames():
            name = list(keys.keys())[list(keys.values()).index(i['champion'])]
            recentChamps = recentChamps + " " + name
        wordcloud = WordCloud(color_func=self.randomColor,
                              width=1920, height=1080).generate(recentChamps)
        plt.axis("off")

        plt.imshow(wordcloud.recolor(color_func=self.randomColor, random_state=1),
                   interpolation="bilinear")
        wordcloud.to_file('./RecentlyPlayed/'+self.SummonerName+'.png')
        plt.figure()

        # plt.show()
        # plt.savefig()


if __name__ == "__main__":
    lp = LeagueProfile(
        "RGAPI-5cb32e57-c3e9-4712-be4f-eb09c9f71a49", 'BIG SQUEEZER')
    # x = lp.getOldestPlayedChampions()
    lp.getRecentGamesPlayedWordCloud()

    # lp.getRecentGamesPlayedWordCloud()

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


class LeagueProfile():
    ProfileData = {}
    RiotApiKey = "RGAPI-a3cb1641-3b01-4fbc-825b-f42511be5088"
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
    lp.getRecentGamesPlayedWordCloud()

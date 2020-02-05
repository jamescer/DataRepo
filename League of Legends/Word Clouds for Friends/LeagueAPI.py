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


class LeagueAPI():
    RiotApiKey = ''
    ProfileData = {}
    SummonerName = ""
    SummonerNameUrl = ''
    MatchHistory = {}
    ChampionKeys = {
        "Aatrox": 266,
        "266": "Aatrox",
        "Ahri": 103,
        "103": "Ahri",
        "Akali": 84,
        "84": "Akali",
        "Alistar": 12,
        "12": "Alistar",
        "Amumu": 32,
        "32": "Amumu",
        "Anivia": 34,
        "34": "Anivia",
        "Annie": 1,
        "1": "Annie",
        "Aphelios": 523,
        "523": "Aphelios",
        "Ashe": 22,
        "22": "Ashe",
        "AurelionSol": 136,
        "136": "AurelionSol",
        "Azir": 268,
        "268": "Azir",
        "Bard": 432,
        "432": "Bard",
        "Blitzcrank": 53,
        "53": "Blitzcrank",
        "Brand": 63,
        "63": "Brand",
        "Braum": 201,
        "201": "Braum",
        "Caitlyn": 51,
        "51": "Caitlyn",
        "Camille": 164,
        "164": "Camille",
        "Cassiopeia": 69,
        "69": "Cassiopeia",
        "Chogath": 31,
        "31": "Chogath",
        "Corki": 42,
        "42": "Corki",
        "Darius": 122,
        "122": "Darius",
        "Diana": 131,
        "131": "Diana",
        "Draven": 119,
        "119": "Draven",
        "DrMundo": 36,
        "36": "DrMundo",
        "Ekko": 245,
        "245": "Ekko",
        "Elise": 60,
        "60": "Elise",
        "Evelynn": 28,
        "28": "Evelynn",
        "Ezreal": 81,
        "81": "Ezreal",
        "Fiddlesticks": 9,
        "9": "Fiddlesticks",
        "Fiora": 114,
        "114": "Fiora",
        "Fizz": 105,
        "105": "Fizz",
        "Galio": 3,
        "3": "Galio",
        "Gangplank": 41,
        "41": "Gangplank",
        "Garen": 86,
        "86": "Garen",
        "Gnar": 150,
        "150": "Gnar",
        "Gragas": 79,
        "79": "Gragas",
        "Graves": 104,
        "104": "Graves",
        "Hecarim": 120,
        "120": "Hecarim",
        "Heimerdinger": 74,
        "74": "Heimerdinger",
        "Illaoi": 420,
        "420": "Illaoi",
        "Irelia": 39,
        "39": "Irelia",
        "Ivern": 427,
        "427": "Ivern",
        "Janna": 40,
        "40": "Janna",
        "JarvanIV": 59,
        "59": "JarvanIV",
        "Jax": 24,
        "24": "Jax",
        "Jayce": 126,
        "126": "Jayce",
        "Jhin": 202,
        "202": "Jhin",
        "Jinx": 222,
        "222": "Jinx",
        "Kaisa": 145,
        "145": "Kaisa",
        "Kalista": 429,
        "429": "Kalista",
        "Karma": 43,
        "43": "Karma",
        "Karthus": 30,
        "30": "Karthus",
        "Kassadin": 38,
        "38": "Kassadin",
        "Katarina": 55,
        "55": "Katarina",
        "Kayle": 10,
        "10": "Kayle",
        "Kayn": 141,
        "141": "Kayn",
        "Kennen": 85,
        "85": "Kennen",
        "Khazix": 121,
        "121": "Khazix",
        "Kindred": 203,
        "203": "Kindred",
        "Kled": 240,
        "240": "Kled",
        "KogMaw": 96,
        "96": "KogMaw",
        "Leblanc": 7,
        "7": "Leblanc",
        "LeeSin": 64,
        "64": "LeeSin",
        "Leona": 89,
        "89": "Leona",
        "Lissandra": 127,
        "127": "Lissandra",
        "Lucian": 236,
        "236": "Lucian",
        "Lulu": 117,
        "117": "Lulu",
        "Lux": 99,
        "99": "Lux",
        "Malphite": 54,
        "54": "Malphite",
        "Malzahar": 90,
        "90": "Malzahar",
        "Maokai": 57,
        "57": "Maokai",
        "MasterYi": 11,
        "11": "MasterYi",
        "MissFortune": 21,
        "21": "MissFortune",
        "MonkeyKing": 62,
        "62": "MonkeyKing",
        "Mordekaiser": 82,
        "82": "Mordekaiser",
        "Morgana": 25,
        "25": "Morgana",
        "Nami": 267,
        "267": "Nami",
        "Nasus": 75,
        "75": "Nasus",
        "Nautilus": 111,
        "111": "Nautilus",
        "Neeko": 518,
        "518": "Neeko",
        "Nidalee": 76,
        "76": "Nidalee",
        "Nocturne": 56,
        "56": "Nocturne",
        "Nunu": 20,
        "20": "Nunu",
        "Olaf": 2,
        "2": "Olaf",
        "Orianna": 61,
        "61": "Orianna",
        "Ornn": 516,
        "516": "Ornn",
        "Pantheon": 80,
        "80": "Pantheon",
        "Poppy": 78,
        "78": "Poppy",
        "Pyke": 555,
        "555": "Pyke",
        "Qiyana": 246,
        "246": "Qiyana",
        "Quinn": 133,
        "133": "Quinn",
        "Rakan": 497,
        "497": "Rakan",
        "Rammus": 33,
        "33": "Rammus",
        "RekSai": 421,
        "421": "RekSai",
        "Renekton": 58,
        "58": "Renekton",
        "Rengar": 107,
        "107": "Rengar",
        "Riven": 92,
        "92": "Riven",
        "Rumble": 68,
        "68": "Rumble",
        "Ryze": 13,
        "13": "Ryze",
        "Sejuani": 113,
        "113": "Sejuani",
        "Senna": 235,
        "235": "Senna",
        "Sett": 875,
        "875": "Sett",
        "Shaco": 35,
        "35": "Shaco",
        "Shen": 98,
        "98": "Shen",
        "Shyvana": 102,
        "102": "Shyvana",
        "Singed": 27,
        "27": "Singed",
        "Sion": 14,
        "14": "Sion",
        "Sivir": 15,
        "15": "Sivir",
        "Skarner": 72,
        "72": "Skarner",
        "Sona": 37,
        "37": "Sona",
        "Soraka": 16,
        "16": "Soraka",
        "Swain": 50,
        "50": "Swain",
        "Sylas": 517,
        "517": "Sylas",
        "Syndra": 134,
        "134": "Syndra",
        "TahmKench": 223,
        "223": "TahmKench",
        "Taliyah": 163,
        "163": "Taliyah",
        "Talon": 91,
        "91": "Talon",
        "Taric": 44,
        "44": "Taric",
        "Teemo": 17,
        "17": "Teemo",
        "Thresh": 412,
        "412": "Thresh",
        "Tristana": 18,
        "18": "Tristana",
        "Trundle": 48,
        "48": "Trundle",
        "Tryndamere": 23,
        "23": "Tryndamere",
        "TwistedFate": 4,
        "4": "TwistedFate",
        "Twitch": 29,
        "29": "Twitch",
        "Udyr": 77,
        "77": "Udyr",
        "Urgot": 6,
        "6": "Urgot",
        "Varus": 110,
        "110": "Varus",
        "Vayne": 67,
        "67": "Vayne",
        "Veigar": 45,
        "45": "Veigar",
        "Velkoz": 161,
        "161": "Velkoz",
        "Vi": 254,
        "254": "Vi",
        "Viktor": 112,
        "112": "Viktor",
        "Vladimir": 8,
        "8": "Vladimir",
        "Volibear": 106,
        "106": "Volibear",
        "Warwick": 19,
        "19": "Warwick",
        "Xayah": 498,
        "498": "Xayah",
        "Xerath": 101,
        "101": "Xerath",
        "XinZhao": 5,
        "5": "XinZhao",
        "Yasuo": 157,
        "157": "Yasuo",
        "Yorick": 83,
        "83": "Yorick",
        "Yuumi": 350,
        "350": "Yuumi",
        "Zac": 154,
        "154": "Zac",
        "Zed": 238,
        "238": "Zed",
        "Ziggs": 115,
        "115": "Ziggs",
        "Zilean": 26,
        "26": "Zilean",
        "Zoe": 142,
        "142": "Zoe",
        "Zyra": 143,
        "143": "Zyra"
    }

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

    def getMatchInfo(self):
        '''
        Keys:
        {"gameId": 3286979659,
            "gameStartTime": 1580922772369,
            "platformId": "NA1",
            "gameMode": "CLASSIC",
            "mapId": 11,
            "gameType": "MATCHED_GAME",
            "gameQueueConfigId": 440,
            "observers":{}
            "participants":[{},{},{}],
            "gameLength": 1000,
            "bannedChampions":[{"teamId": 100,
            "championId": 157,
            "pickTurn": 1},{},{}]
            }
        '''
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

    def getCurrentGame(self):
        with urllib.request.urlopen('https://na1.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/'+self.ProfileData['id'] + "?api_key=" + self.RiotApiKey) as url:
            return json.loads(url.read().decode())

    def getOldestPlayedChampions(self):
        championDict = self.getChampionMasteriesBySummonerId()
        arr2 = championDict
        # Saving Mastery array json array to folder
        with open('./OldestChamps/'+lp.SummonerName+'-Mstry.json', 'w') as outfile:
            json.dump(arr2, outfile)
        newDict = {}
        newarr = []

        for i in championDict:
            # Get champion from list
            name = list(self.ChampionKeys.keys())[
                list(self.ChampionKeys.values()).index(i['championId'])]
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

        # Save oldest champs obtained mastery with JSON data to folder
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
    leeg = LeagueAPI(
        "RGAPI-5cb32e57-c3e9-4712-be4f-eb09c9f71a49", 'boytimwunda')

    with open('./curgame.json', encoding="utf8") as json_file:
        curgame = json.load(json_file)

    for i in curgame['bannedChampions']:
        print(leeg.ChampionKeys[str(i['championId'])])

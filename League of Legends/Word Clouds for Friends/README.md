# WordClouds
## Section is meant to take data that is normally in a string format or where a lot of words are used and visualize in a fun way to see the most abundant words used.

## Technologies Used
I used [Riot Games API](https://developer.riotgames.com/) to pull and analyze data in a json format.

## LeagueProfile.py 

### Using the LeagueProfile class:
To initialize a LeagueProfile class, simply put in the riot api key you have and the summoner name you'd like to lookup\
Example:
```python
lp = LeagueProfile('this-is-your-riot-api-key-eb09','TToXiiK')
```

### Methods inside the League profile class
There are a few methods inside the class used to obtain summoner data

Get champs you
Example:
```python
lp = LeagueProfile('TToXiiK')
x = lp.getOldestPlayedChampions()
print(x[0])
```
Output:
```json
{
    "name": "Udyr",
    "masteryPoints": 4442,
    "lastDate": "2016-04-02 01:38:55",
    "datev2": "Sat, 02 Apr 2016 01:38:55 +0000",
    "epoch": 1459575535000
}
```

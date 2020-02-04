import json

filename = 'ChampionKeys.json'
filename2 = 'DDragonData.json'
with open(filename2, encoding="utf8") as json_file:
    data = json.load(json_file)

data2 = {}
for i in data['data']:
    # print(i)
    # print(data['data'][i])
    data2.update({data['data'][i]['id']: {'id': data['data'][i]['id'],
                                          'name': data['data'][i]['id'],
                                          'key': int(data['data'][i]['key'])}
                  })

with open(filename, 'w') as outfile:
    json.dump(data2, outfile)

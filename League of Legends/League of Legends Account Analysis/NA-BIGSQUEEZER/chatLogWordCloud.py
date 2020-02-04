
import matplotlib.pyplot as plt
import os
from wordcloud import WordCloud
import json
# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
# Get all jsons -> get all chats from jsons -> generate owrd cloud from json - > see toxicity ensue
all_words = ""

path = './leagueoflegends/chatLogs/'
for filename in os.listdir(path):
    # print(filename)
    with open(path + str(filename)) as json_file:
        data = json.load(json_file)
    for i in data['text']:
        # print(i)
        all_words = all_words + " " + str(i['chat'])
    # print(data)


def randomColor(word, font_size, position, orientation, random_state=None,
                **kwargs):
    import random
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb2 = [r, g, b]
    return tuple(rgb2)


print(all_words)
# Generate a word cloud image
wordcloud = WordCloud(color_func=randomColor, height=1080,
                      width=1920).generate(all_words)

# Display the generated image:
# the matplotlib way:
plt.axis("off")
plt.imshow(wordcloud, interpolation='bilinear')



import matplotlib.pyplot as plt
import os
from wordcloud import WordCloud
import json

all_words = ""

path = './tickets/'
for filename in os.listdir(path):
    # print(filename)
    with open(path + str(filename)) as json_file:
        data = json.load(json_file)
    for i in data['comments']:
        # print(i)
        if i['author'] == "Agent":
            all_words = all_words + " " + str(i['comment'])
    # print(data)


def randomColor(word, font_size, position, orientation, random_state=None,
                **kwargs):
    import random
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb2 = [r, g, b]
    return tuple(rgb2)


# print(all_words)
# Generate a word cloud image
wc = WordCloud(color_func=randomColor, height=1080,
                      width=1920,max_words=1200000).generate(all_words)

plt.imshow(wc.recolor(color_func=randomColor, random_state=1),
           interpolation="bilinear")
wc.to_file("SupportTicketWordCloud.png")
plt.axis("off")
plt.figure()


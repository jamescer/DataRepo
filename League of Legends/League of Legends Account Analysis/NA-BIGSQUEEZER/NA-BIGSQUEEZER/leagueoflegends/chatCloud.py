
import matplotlib.pyplot as plt
import json
import os
from os import path
from wordcloud import WordCloud
import random
path = './chatLogs/'
all_words = ''

for filename in os.listdir(path):

    with open('./chatLogs/'+filename) as json_file:
        data = json.load(json_file)
        for i in data['text']:
            all_words = all_words + ' ' + i['chat']

# print(all_words)
# Generate a word cloud image

wordcloud = WordCloud().generate(all_words)
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis("off")

# plt.figure()
# plt.imshow(wordcloud, interpolation="bilinear")
# plt.axis("off")
# plt.show()


def grey_color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    rgbl = [255, 0, 0]
    x = random.randrange(0, 255)
    y = random.randrange(0, 255)
    z = random.randrange(0, 255)
    rgbl = [x, y, z]
    return tuple(rgbl)

    # return "hsl(0, 0%%, %d%%)" % random.randint(0, 255)
wc = WordCloud(max_words=10000, width=1920, height=1080,
               random_state=1).generate(all_words)
plt.imshow(wc.recolor(color_func=grey_color_func, random_state=1),
           interpolation="bilinear")
wc.to_file("a_new_hope.png")
plt.axis("off")
plt.figure()

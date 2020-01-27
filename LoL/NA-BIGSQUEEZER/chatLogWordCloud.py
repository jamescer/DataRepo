
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

print(all_words)
# Generate a word cloud image
wordcloud = WordCloud().generate(all_words)

# Display the generated image:
# the matplotlib way:

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

# lower max_font_size
wordcloud = WordCloud(max_font_size=40).generate(all_words)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

# The pil way (if you don't have matplotlib)
# image = wordcloud.to_image()
# image.show()

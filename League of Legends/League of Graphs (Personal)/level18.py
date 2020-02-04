import numpy as np
import json
import pandas as pd
import matplotlib.pyplot as plt



with open('data.json',encoding="utf8") as json_file:
    data = json.load(json_file)

champions = data['data']
level_18 = 18

for i in champions:
    print(champions[i].keys())
    break

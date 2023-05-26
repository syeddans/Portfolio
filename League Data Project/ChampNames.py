import json
import pandas as pd

with open("Champion.json", "r") as json_file:
    data = json.load(json_file)

v = data["data"].values()
champion_names = []
for x in v:
    champion_names.append(x['id'])

df = pd.DataFrame({'Champion': champion_names})
df.to_csv("ChampionNames.csv", index=False)


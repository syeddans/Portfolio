import pandas as pd

# Read the first CSV file
df1 = pd.read_csv("ChampionNames.csv")
df2 = pd.read_csv("Games50averages.csv")
df3 = pd.read_csv("Games100averages.csv")
df4 = pd.read_csv("Games150averages.csv")
df5 = pd.read_csv("Games250averages.csv")

result1 = pd.merge(df1, df2, on='Champion', how='left')
result2 = pd.merge(result1, df3, on='Champion', how='left')
result3 = pd.merge(result2, df4, on='Champion', how='left')
final_result = pd.merge(result3, df5, on='Champion', how='left')
final_result = final_result.fillna(0)
final_result.to_csv("MasterData.csv", index=False)




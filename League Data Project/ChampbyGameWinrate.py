import pandas as pd

#games500 not included as not enough games in the season so far
fileNames= ["Games50", "Games100", "Games150", "Games250"]

for x in fileNames:
    df1 = pd.read_csv(f'{x}.csv')
    df2 = pd.DataFrame(columns=df1.columns)
    df_grouped = df1.groupby('Champion').mean()
    df_grouped = df_grouped.iloc[:, 3]
    df_grouped.to_csv(f'{x}averages.csv')





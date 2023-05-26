import pandas as pd

df1 = pd.read_csv("ChampData.csv")
games50 = pd.DataFrame(columns=df1.columns)
games100 = pd.DataFrame(columns=df1.columns)
games150 = pd.DataFrame(columns=df1.columns)
games250 = pd.DataFrame(columns=df1.columns)
games500 = pd.DataFrame(columns=df1.columns)


games50 = games50.append(df1[(df1['Games Played'] >= 50) & (df1['Games Played'] <= 100)], ignore_index=True)
print("50 done")
games100 = games100.append(df1[(df1['Games Played'] >= 100) & (df1['Games Played'] <= 150)], ignore_index=True)
print("100 done")
games150 = games150.append(df1[(df1['Games Played'] >= 150) & (df1['Games Played'] <= 250)], ignore_index=True)
print("150 done")
games250 = games250.append(df1[(df1['Games Played'] >= 250) & (df1['Games Played'] <= 500)], ignore_index=True)
print("250 done")
games500 = games500.append(df1[(df1['Games Played'] >= 500)], ignore_index=True)
print("500 done")

games50.sort_values(by=['Champion']).to_csv('Games50.csv')
games100.sort_values(by=['Champion']).to_csv('Games100.csv')
games150.sort_values(by=['Champion']).to_csv('Games150.csv')
games250.sort_values(by=['Champion']).to_csv('Games250.csv')
games500.sort_values(by=['Champion']).to_csv('Games500.csv')


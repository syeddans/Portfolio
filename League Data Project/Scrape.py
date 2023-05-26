from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import pandas as pd


summoner_Names_Column = []
champion_Name_Column = []
champion_Games_Played_Column = []
champion_Winrate_Column = []

df = pd.read_csv("SummonerNames.csv")
for y in range(0,len(df)):
    print(df.iloc[y, 1].encode('utf8'))
    req = Request(
        url= f'https://www.leagueofgraphs.com/summoner/champions/na/{df.iloc[y, 1]}'.replace(" ", "%20"),
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    try:
        html_text = urlopen(req).read()
    except:
        print("pass")
    soup = BeautifulSoup(html_text, 'lxml')
    champion = soup.find_all('tr')


    for x in range(1,len(champion)):
        try:
            champion_name = champion[x].find('span', class_='name').text.strip()
            summoner_Names_Column.append(df.iloc[y, 1])
            champion_Name_Column.append(champion_name)

            champion_games = champion[x].find_all('a', class_="full-cell")
            champion_games_full_string = str(champion_games[0]).split()[16]
            champion_games_num_string = champion_games_full_string.split("=")
            champion_games_played = int(champion_games_num_string[1][1:-1])
            champion_Games_Played_Column.append(champion_games_played)

            champion_winrate_full_string = str(champion_games[1]).split()[16]
            champion_winrate_num_string = champion_winrate_full_string.split("=")
            champion_winrate = int(float(champion_winrate_num_string[1][1:-1])*100)
            champion_Winrate_Column.append(champion_winrate)
        except AttributeError:
            break

df2 = pd.DataFrame()
df2['Champion'] = champion_Name_Column
df2['Games Played'] = champion_Games_Played_Column
df2['Winrate(%)'] = champion_Winrate_Column
df2['From Summoner'] = summoner_Names_Column
df2.to_csv('ChampData.csv')


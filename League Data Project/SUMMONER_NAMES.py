import requests
import time
import csv
import pandas as pd
api_key = 'RGAPI-7523f0c1-84e3-4395-846e-dee09ae5d5e5'
summonerNames = []

def get_summonerNames(url):
    response = requests.get(url)
    data = response.json()
    #print(data)
    if data == []:
        return False
    else:
        for x in data:
            summonerNames.append([x['summonerName']])

def summoners():
        request_number = 0
        for x in range(0,7):
            for page in range(1, 9999):
                urls = [
                    "https://na1.api.riotgames.com/lol/league-exp/v4/entries/RANKED_SOLO_5x5/CHALLENGER/I?page=" + str(
                        page) + f'&api_key={api_key}',
                    "https://na1.api.riotgames.com/lol/league-exp/v4/entries/RANKED_SOLO_5x5/GRANDMASTER/I?page=" + str(
                        page) + f'&api_key={api_key}',
                    "https://na1.api.riotgames.com/lol/league-exp/v4/entries/RANKED_SOLO_5x5/MASTER/I?page=" + str(
                        page) + f'&api_key={api_key}',
                    "https://na1.api.riotgames.com/lol/league-exp/v4/entries/RANKED_SOLO_5x5/DIAMOND/I?page=" + str(
                        page) + f'&api_key={api_key}',
                    "https://na1.api.riotgames.com/lol/league-exp/v4/entries/RANKED_SOLO_5x5/DIAMOND/II?page=" + str(
                        page) + f'&api_key={api_key}',
                    "https://na1.api.riotgames.com/lol/league-exp/v4/entries/RANKED_SOLO_5x5/DIAMOND/III?page=" + str(
                        page) + f'&api_key={api_key}',
                    "https://na1.api.riotgames.com/lol/league-exp/v4/entries/RANKED_SOLO_5x5/DIAMOND/IV?page=" + str(
                        page) + f'&api_key={api_key}']
                url = urls[x]
                print(url)
                request_number+=1
                if request_number ==99:
                    time.sleep(120)
                if get_summonerNames(url) is False:
                    #print(summonerNames)
                    break;

        df = pd.DataFrame(summonerNames, columns=['Summoner_Name'])
        df.to_csv('SummonerNames.csv')



summoners()

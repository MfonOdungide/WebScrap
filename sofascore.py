import pandas as pd
import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.soccerbase.com/teams/home.sd'
r = requests.get(url)
soup = bs(r.content, 'html.parser')
teams = soup.find('div', {'class': 'headlineBlock'}, text='Team').next_sibling.find_all('li')

teams_dict = {}
for team in teams:
    link = 'https://www.soccerbase.com' + team.find('a')['href']
    team = team.text

    teams_dict[team] = link

consolidated = []
for k, v in teams_dict.items():
    print('Acquiring %s data...' % k)

    headers = ['Team', 'Competition', 'Home Team', 'Home Score', 'Away Team', 'Away Score', 'Date Keep']
    r = requests.get('%s&teamTabs=results' % v)
    soup = bs(r.content, 'html.parser')

    h_scores = [int(i.text) for i in soup.select('.score a em:first-child')]
    a_scores = [int(i.text) for i in soup.select('.score a em + em')]

    limit = len(a_scores)
    team = [k for i in soup.select('.tournament', limit=limit)]
    comps = [i.text for i in soup.select('.tournament a', limit=limit)]
    dates = [i.text for i in soup.select('.dateTime .hide', limit=limit)]
    h_teams = [i.text for i in soup.select('.homeTeam a', limit=limit)]
    a_teams = [i.text for i in soup.select('.awayTeam a', limit=limit)]

    df = pd.DataFrame(list(zip(team, comps, h_teams, h_scores, a_teams, a_scores, dates)),
                      columns=headers)
    consolidated.append(df)

pd.concat(consolidated)(r'#your file location address sep=',', encoding='utf-8-sig', index=False)
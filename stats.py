from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import os
import threading
import unicodedata

def remove(string):
    return string.replace (" ","") or ("%20","")
myurl = remove('http://www.statarea.com/compare/teams/Spal(Italy)/Pescara(Italy)')
# myurl = remove('http://www.statarea.com/compare/teams/Vila+Nova(Brazil)/Botafogo+PB(Brazil)')
# myurl = remove('http://www.statarea.com/compare/teams/Andorra(Andorra)/Latvia(Latvia)')
uClient = uReq(myurl)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")#.get_text(strip=True)

matchsummaryfacts = page_soup.findAll("div",{"class":"facts"})
lastteamsmatches = page_soup.findAll("div",{"class":"lastteamsmatches"})
teamstatistics = page_soup.findAll("div",{"class":"teamsstatistics"})
teambetstatistics = page_soup.findAll("div",{"class":"teamsbetstatistics"})
# print(len(teamstatistics))
# print (teamstatistics)

class displayResult:
    dash = '==============================================='
    dott = '...............................................'
    

    def longLine(self):
        print(self.dash)
    def dots(self):
        print(self.dott)
    def result(self,*args):
        self.dots()
        # print("Competition" + args[0])
        print(f'''		{args[0]}
		Time     = {args[1]} 
		Teams    = {args[2]} 
		Link = {args[2]}''')
        self.dots()
  
def SummaryFacts():
    print('-------------------------------')
    print ('Summary Match Facts')
    print('-------------------------------')
    for summarymatchfacts in matchsummaryfacts:
    # Finding the summary of the matches
        summary = summarymatchfacts.findAll ("div", {"class":"value"})
        # print(len(summary))
        summarychart = summarymatchfacts.findAll ("div", {"class":"chart"})
        TotalMatches = summary[0].text
        HomeWins = summary[1].text
        AwayWins = summary[2].text
        DrawMatch = summary[3].text
        str_summarychart = (summarychart[0].text)
        # print(str_summarychart)
        list_chart1 = []
        list_chart1.append(str_summarychart)
        
        # print ('Listchar1 =' + str(list_chart1))
        list_chartFind = str(list_chart1).replace(u'\\xa0','0%')
        
        cl1 = list_chartFind.replace(u'[\'','') 
        list_clean = cl1.replace(u'\']','')
        chart = (list_clean).split("%",3)
        Home = chart[0]
        Draw = chart[1]
        Away = chart[2]

        print("Total Number of Matches:" + TotalMatches)
        print("Home Wins:" + HomeWins)
        print("Away Wins:" + AwayWins)
        print("Draw Matches:" + DrawMatch)
        print(" Home " + " Draw " + " Away")
        print("  "+ Home +"%  " + Draw +"%    "+ Away + "%    ")

def Last10TeamMatches():
    print('-------------------------------')
    print ('Last 10 Team Matches')
    print('-------------------------------')

    for results in lastteamsmatches:
        matchitem = results.findAll ("div", {"class":"matchitem"}) #all 10 match details each
    for FTgoals in matchitem:
        FT = FTgoals.findAll ("div", {"class":"goals"})
        FT_awaygoal = FT[1].text
        FT_homegoal = FT[0].text
        FullTime = 'FullTime ' + FT_homegoal +' : ' + FT_awaygoal
        print(FullTime)
        
        matchdetails = results.findAll ("div", {"class":"details"})
        # print('===============================')
        
    for rows in matchdetails:

        actions = rows.findAll ("div", {"class":"player"}) or rows.findAll ("div", {"class":"noaction"})
    # for halftime in matchdetails:
        HT = rows.findAll ("div", {"class":"goals"})
        awaygoal = HT[0].text
        homegoal = HT[1].text
        maxaction = len(actions)
        print('******************')
        # print('FullTime ' + FT_homegoal +' : ' + FT_awaygoal)
        HalfTime = 'HalfTime ' + homegoal +' : ' + awaygoal
        print(HalfTime)

        for i in range (maxaction):
            print(actions[i].text)
            goals = actions[i].text
            # for Matchresult in matchitem:
            # FT = Matchresult.findAll ("div", {"class":"goals"})
            # FT_awaygoal = FT[1].text
            # FT_homegoal = FT[0].text
        # print('FullTime ' + FT_homegoal +' : ' + FT_awaygoal)
        # disp.result(HalfTime,FullTime,goals)

def Last10Facts():
    for statisticsFacts in teamstatistics:
            row2 = statisticsFacts.findAll ("div", {"class":"value"})
            print('-------------------------------')
            print ('Facts for Last 10 Matches')
            print('-------------------------------')
            print('                 Home     Away')
            print('Win                ' + row2[0].text + '        ' + row2[13].text)
            print('Draw               ' + row2[1].text + '        ' + row2[14].text)
            print('Lose               ' + row2[2].text + '        ' + row2[15].text)
            print('Avg. scored goal   ' + row2[3].text + '        ' + row2[16].text)
            print('Avg. conceed goal  ' + row2[4].text + '        ' + row2[17].text)
            print('Score chance       ' + row2[5].text + '        ' + row2[18].text)
            print('Conceed chance     ' + row2[6].text + '        ' + row2[19].text)
            print('Clean sheet        ' + row2[7].text + '        ' + row2[20].text)
            print('Not score          ' + row2[8].text + '        ' + row2[21].text)
            print('Over 2.5           ' + row2[9].text + '        ' + row2[22].text)
            print('Under 2.5          ' + row2[10].text + '        ' + row2[23].text)
            print('Time No Score      ' + row2[11].text + '        ' + row2[24].text)
            print('Time No Conceed    ' + row2[12].text + '        ' + row2[25].text)
            # print('===============================')

def Last10Statistics():
    for statisticsFacts in teambetstatistics:
        row2 = statisticsFacts.findAll ("div", {"class":"value"})
        total = len(row2)
        Home_HomeWins = row2[0].text
        Home_Draw = row2[1].text
        Home_AwayWins = row2[2].text
        Away_HomeWins = row2[88].text
        Away_Draw = row2[89].text
        Away_AwayWins = row2[90].text
        print('-------------------------------')
        print ('Statistics for Last 10 Matches')
        print('-------------------------------')
        print('Home Wins    '+ Home_HomeWins + ' : ' + 'Away Wins   '+ Away_HomeWins)
        print('Draw Wins    '+ Home_Draw + ' : ' + 'Away Draw   '+ Away_Draw)
        print('Away Wins    '+ Home_AwayWins + ' : ' + 'Home Wins   '+ Away_AwayWins)
        
        # *****************************************
        # use this to verify the statistic number tags
        # --------------------------------------------
        # for i in range(len(row2)):
        #     count = i
        #     print(str(count) + ': ' + row2[i].text)
        # print(len(row2))
        # 0, 1, 2 --> 88, 89, 90
        # 85, 86, 87 --> 173, 174, 175
        # 15mins Winner --> [64,65,66],[152,153,154] (64+88...)
        # 30mins Winner -->[67,68,69],[155,156,157]
        # 45mins Winner -->[70,71,72],[158,159,160]
        # 0-15mins --> [29],[117]
        # 16-30mins -->[30],[118]
        # 31-45mins -->[31],[119]
        # ******************************************


def main():
    SummaryFacts()
    # Last10TeamMatches()
    # threading.Thread(Last10Facts()).start
    # threading.Thread(Last10Statistics())







if __name__ == '__main__': main()
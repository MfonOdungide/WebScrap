from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import os

def remove(string):
    return string.replace (" ","")

myurl = remove('http://www.statarea.com/compare/teams/Vila+Nova(Brazil)/Botafogo+PB(Brazil)')
uClient = uReq(myurl)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

matchsummary = page_soup.findAll("div",{"class":"facts"})
lastteamsmatches = page_soup.findAll("div",{"class":"lastteamsmatches"})
# print(len(match))
# print (match)

for summarymatchfacts in matchsummary:
    # Finding the summary of the matches
    row1 = summarymatchfacts.findAll ("div", {"class":"value"})
    # print(row1)
    TotalMatches = row1[0].text
    HomeWins = row1[1].text
    AwayWins = row1[2].text
    DrawMatch = row1[3].text
    
    # # try:
    #     pass
    # except expression as identifier:
    #     pass


    # print("Total Number of Matches:" + TotalMatches)
    # print("Home Wins:" + HomeWins)
    # print("Away Wins:" + AwayWins)
    # print("Draw Matches:" + DrawMatch)

for results in lastteamsmatches:
    count = 0

    matchitem = results.findAll ("div", {"class":"matchitem"}) #all 10 match details each
    
    for Matchresult in matchitem:
        FT = Matchresult.findAll ("div", {"class":"goals"})
        FT_awaygoal = FT[1].text
        FT_homegoal = FT[0].text

    matchdetails = results.findAll ("div", {"class":"details"})
    print('===============================')
   
    # print (len(matchitem))
    # print(len(matchdetails))
    # print(matchdetails[0].text)
    # print(matchrow)
    # print(matchitem)
    # print (row1[2].text)  
        

     
        # print(homegoal +' : ' + awaygoal)
        # HT = halftime.findAll ("div", {"class":"goals"})
        # awaygoal = HT[0].text
        # homegoal = HT[1].text
        
    maxaction = len(actions)
    print('******************')
    print('HalfTime ' + homegoal +' : ' + awaygoal)
        
    for i in range (maxaction):
        print(actions[i].text) 
for rows in matchdetails:

    actions = rows.findAll ("div", {"class":"player"}) or rows.findAll ("div", {"class":"noaction"})
    # for halftime in matchdetails:
    HT = rows.findAll ("div", {"class":"goals"})
    awaygoal = HT[0].text
    homegoal = HT[1].text
    print('FullTime ' + FT_homegoal +' : ' + FT_awaygoal)

                



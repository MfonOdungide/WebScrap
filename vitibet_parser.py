from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re

myurl = 'https://www.vitibet.com/index.php?clanek=quicktips_toptips&sekce=fotbal&lang=en'

uClient = uReq(myurl)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")
container = page_soup.findAll("div",{"id": "quicktips"})
filename = "vitibet.csv"
f = open (filename, "w")

headers = "Date, HomeTeam, AwayTeam, HomeWin, Draw, AwayWin, TipIndex, HomeScore, AwayScore, Tip \n"
f.write (headers)
for daymatches in container:
	matches = page_soup.findAll("tr")
	
	for select_matches in matches:
		# team_match1 = select_matches.findAll("td",{"class": "barvapodtipek1"})
		team_match1 = select_matches.findAll("td",{"class": "standardbunka"})
		team_match2 = select_matches.findAll("td",{"class": "vetsipismo"})
		team_match3 = select_matches.findAll("td",{"class": "barvapodtipek1"}) or select_matches.findAll("td",{"class": "barvapodtipek2"})
		# print("Date1:" + str(team_match1[0].text))
		# print("Date1:" + str(select_matches[0].text))

		# team_matches = len(team_match1)
		# print("TeamMatch:" + str(team_match1))
		count= 0
		count2 = 0
		count3 =0
# HomeTeam = team_match1[0].text
		for pick_matches in team_match1:
			

			# standardX = pick_matches.findAll("td",{"class": "standardbunka"})
			# print("PickMatch:" + str(pick_matches.text))
			# print("Date:" + str(team_match1[0].text))
			# print("Home:" + str(team_match1[1].text))


		# 	print("A:" + str(pick_matches))
		# 	# print("Tip:" + str(standardX))
			
		# 	# standardX = pick_matches.findAll("td",{"class": "barvapodtipek1"})
			
		# 	for picks in standardX:

			# Date = team_match1[0].text
			# HomeTeam = team_match1[1].text
			# HomeTeam = team_match1[2].text

			Date = team_match1[0].text
			HomeTeam = team_match1[1].text
			AwayTeam = team_match1[2].text
			seperator = team_match1[3].text # parsing the seperator without use
			HomeScore = team_match1[0].text
			AwayScore = team_match1[0].text
			HomeWin = team_match1[4].text
			Draw = team_match1[5].text
			AwayWin = team_match1[6].text
			Tip = team_match1[0].text
			Tip_index = team_match1[7].text




				# print("team_match1[] Length:" + str(Date)) 
			# print("PickMatch Length:" + str(HomeTeam)) 
			# print("HomeTeam: " + HomeTeam)
			# print("AwayTeam: " + AwayTeam )
			# print("Tip: " + Tip)

			# f.write (time + "," + teams +"," + tip + "," + link + "," + "\n")
			
			while count < 1:
				f.write ((Date) + "," + str(HomeTeam) + "," + str(AwayTeam) + "," + str(HomeWin) + "," + str(Draw) + "," + str(AwayWin) + "," + str(Tip_index) + "," )
				count+= 1
				break


		for TeamScore in team_match2:
			HomeScore = team_match2[0].text
			AwayScore = team_match2[1].text

			# print("HomeScore:" + str(HomeScore2))
			# print("AwayScore:" + str(AwayScore2))
			while count2 < 1:
				f.write (str(HomeScore) + "," + str(AwayScore) + ",")
				
				# print("HomeScore:" + str(HomeScore2))
				# f.write (str(Date) + "," + str(HomeTeam) + "," + str(AwayTeam) + "," + str(HomeScore) + "," + str(AwayScore) + "," + str(HomeWin) + "," + str(Draw) + "," + str(AwayWin) + "," + str(Tip) + "," + str(Tip_index) + "," +"\n")
				# print("AwayScore:" + str(AwayScore2))
				count2+= 1
				break	


		for TeamIndex in team_match3:

			Tip = team_match3[0].text
			while count3 < 1:
				f.write (str(Tip) + "," + "\n")
								# f.write (str(Date) + "," + str(HomeTeam) + "," + str(AwayTeam) + "," + str(HomeScore) + "," + str(AwayScore) + "," + str(HomeWin) + "," + str(Draw) + "," + str(AwayWin) + "," + str(Tip) + "," + str(Tip_index) + "," +"\n")
				# print("AwayScore:" + str(AwayScore2))
				count3+= 1
				break	
f.close()

		
			# print("PickMatch Length:" + str(Date))
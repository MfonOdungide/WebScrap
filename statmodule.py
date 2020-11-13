from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import os

myurl = 'http://www.statarea.com/predictions'
uClient = uReq(myurl)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

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
		Tip      = {args[3]}
		HomeWin  = {args[5]} 
		Draw 	 = {args[6]} 
		AwayWin  = {args[7]}
		HT1      = {args[8]} 
		HTX    	 = {args[9]} 
		HT2      = {args[10]}
		Over 1.5 = {args[11]} 
		Over 2.5 = {args[12]} 
		Over 3.5 = {args[13]}
		GG    	 = {args[14]}
		NGG    	 = {args[15]}
		Link = {args[4]}''')
        self.dots()
        # self.longLine()

class File:
	filename = "competitions.csv"
	
	def FileWrite(self):
		f = open (filename, "w")

		headers = "competition_name, time, teams, tip, link, p_htx \n"
		f.write (headers)

	def FileExec(self):
		full_path = os.path.realpath(__file__)
		filepath = 'C:\Windows\System32\cmd.exe /c '+ os.path.dirname(full_path) +'\\'+filename 

		os.system (filepath)

def TodayMatches():
	disp = displayResult()
	disp.longLine()
	day_competition = page_soup.findAll("div",{"class":"competition"}) 

	for match_competition in day_competition:

		comp_name = match_competition.findAll ("div", {"class":"name"}) #holding value for all competitions
		competition_name = comp_name[0].text

		competition_matches = match_competition.findAll ("div", {"class":"cmatch"})

		coeficient = match_competition.findAll("div", {"class":"coefrow"})
		#for c_comp in comp_matches
		#comp_matches = match_competition.findAll ("div", {"class":"match"}) #finding all the matches in the competition

		for day_matches in competition_matches:
			team_selection = day_matches.findAll ("div", {"class":"teams"})
			teams = team_selection[0].text

			time = day_matches.div.text
			link = day_matches.a["href"]	

			selection = day_matches.findAll ("div", {"class":"value"})

			tip = selection[0].text

			# time = day_matches.div.text
			link = day_matches.a["href"]	

			selection = day_matches.findAll ("div", {"class":"value"})

			tip = selection[0].text
			for coef in coeficient:
				row1 = coef.findAll ("div", {"class":"coefbox"})
				# row2 = coef.findAll ("div", {"class":"coefbox seperate"})
				# row3 = coef.findAll ("div", {"class":"coefbox last"})
				p_ft1 = row1[11].text
				p_ftx = row1[12].text
				p_ft2 = row1[13].text
				p_ht1 = row1[14].text
				p_htx = row1[15].text
				p_ht2 = row1[16].text
				p_o2 = row1[17].text 
				p_o3 = row1[18].text
				p_o4 = row1[19].text
				p_bts = row1[20].text
				p_ots = row1[21].text
		# return competition_name, time, teams, tip, link,p_ft1,p_ftx,p_ft2,p_ht1,p_htx,p_ht2,p_o2,p_o3,p_o4,p_bts,p_ots 
			disp.result(competition_name, time, teams, tip, link,p_ft1,p_ftx,p_ft2,p_ht1,p_htx,p_ht2,p_o2,p_o3,p_o4,p_bts,p_ots)

def DisplayOldResult():
	disp = displayResult()
	# disp.longLine()
	# competition_name, time, teams, tip, link, p_ft1,p_ftx,p_ft2,p_ht1,p_htx,p_ht2,p_o2,p_o3,p_o4,p_bts,p_ots= TodayMatches()
	# disp.result(competition_name, time, teams, tip, link,p_ft1,p_ftx,p_ft2,p_ht1,p_htx,p_ht2,p_o2,p_o3,p_o4,p_bts,p_ots)

def main():

	TodayMatches()




if __name__ == '__main__': main()
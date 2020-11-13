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
        print(f'''    Competition      = {args[0]:.2f}
    Time         = {args[1]:.2f} % 
    Teams    = {args[2]:.2f} 
    Tip          = {args[3]:.0f} nm
    Link {args[4]}!''')
        self.dots()
        self.longLine()

class File:
	filename = "competitions.csv"
	
	def FileWrite(self):
		f = open (filename, "w")

		headers = "competition_name, time, teams, tip, link, p_htx \n"
		f.write (headers)

	def FileExec(self):
		full_path = os.path.realpath(__file__)
		# filename = 'competitions.csv'
		# print('C:\Windows\System32\cmd.exe /c '+ os.path.dirname(full_path) + '\\'+filename)
		filepath = 'C:\Windows\System32\cmd.exe /c '+ os.path.dirname(full_path) +'\\'+filename 

		os.system (filepath)

class StatareaMatches:
	def TodayMatches(self):
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
			return time, teams, tip, link
		return competition_name
	

def main():




if __name__ == '__main__': main()
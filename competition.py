from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
# import openpyxl
# import xlsxwriter
# myworkbook = openpyxl.load_workbook(path)
# worksheet= myworkbook.get_sheet_by_name('Sheet1')

# for i in range(5,15):

# 	cellref=mysheet.cell(row=i, column=5)
# 	cellref.value=lista[i]

# workbook = xlsxwriter.Workbook('write_data.xlsx')
# worksheet = workbook.add_worksheet()

# worksheet.write(0, 0, 1234)     # Writes an int
# worksheet.write(1, 0, 1234.56)  # Writes a float
# worksheet.write(2, 0, 'Hello')  # Writes a string
# worksheet.write(3, 0, None)     # Writes None
# worksheet.write(4, 0, True)     # Writes a bool

# workbook.close()
myurl = 'http://www.statarea.com/predictions'
# myurl = 'http://www.statarea.com/predictions/date/2020-10-20/'

#opening web connection and fetching page
uClient = uReq(myurl)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

#grab matches
#coeficient = page_soup.findAll("div",{"class":"coefrow"})
filename = "competitions.csv"
f = open (filename, "w")

headers = "competition_name, time, teams, tip, link, p_htx \n"
f.write (headers)

# def competition
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

		time = day_matches.div.text
		link = day_matches.a["href"]	

		selection = day_matches.findAll ("div", {"class":"value"})

		tip = selection[0].text

		
		# f.write (competition_name + "\n"+ "," + time  +"," + teams +"," + tip + "," + link + ","+ ",")

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
	
	print("FT1:" + p_ft1)
	print("FTX: " + p_ftx)
	print("FT2: " + p_ft2 )
	print("HT1: " + p_ht1)

	f.write (p_htx + "," + "\n")
	# f.write (competition_name + "," + time  +"," + teams +"," + tip + "," + link + ","+ p_htx + "," +"\n" )
f.close()

import requests
from bs4 import BeautifulSoup
import json

# json to python object converter
class challenge(object):
	def __init__(self, j):
		self.__dict__ = json.loads(j)

# web scraper
def scrap():
	db =['name', 'points', 'mentor', 'description', 'one-time', 'dead-line']

	url = "https://beta.wikiversity.org/wiki/%D7%9C%D7%99%D7%9E%D7%95%D7%93%D7%99_%D7%9E%D7%97%D7%A9%D7%91%D7%99%D7%9D_%D7%91%D7%A9%D7%99%D7%98%D7%AA_%D7%91%D7%98%D7%90#%D7%A0%D7%99%D7%A0%D7%92'%D7%95%D7%AA"
	page = requests.get(url)
	#print(page.content)
	
	# creating beautiful soup instance
	soup = BeautifulSoup(page.content, 'html.parser')
	#print(soup)
	
	challenges = {}
	titles = soup.find_all('h3')
	for title in titles:
		spams = title.find_all('span', class_="mw-headline")
		#print(spams)
		
		for spam in spams:
			#print(spam)
			
			if("Challenges" in spam.text):
				spam.string = spam.text.replace('Challenges', '').lstrip().rstrip()
				
				#print(spam.text)
				if(spam.text == "Security" or spam.text == "Reversing & Pwning" or spam.text == "Resources"):
					#print(spam.text)
					continue
				#print(spam.text)
				
				challenges[spam.text] = []
				
				table = spam.find_next('table', class_="wikitable")
				if(spam.text == "Python" or spam.text == "Bioinformatics"):	# can't distinguish between the tables
					table = table.find_next('table', class_="wikitable")
				#print(table.text)
				
				for tr in table.find_all("tr")[1:]:		# skiping columns names
					#print(tr.text)
					j = "{"
					for td, column_name in zip(tr.find_all("td"), db):
						#print(repr(td.text.rstrip().replace('"', '\\"')))
						j += '"' + column_name + '"' + ': ' + '"' + td.text.rstrip().replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n') + '", '
						
						#print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
					j = j[:-2] + '}'
					#print(j)
					#print(".............................")
					#print(repr(j))
					
					chall = challenge(j)
					#print(type(chall.points), chall.points)
					#print(challenges.keys())
					challenges[spam.text].append(chall)
					
					#print("###################################")
			
			#print("-----------------------")
		
	
	return challenges

#scrap()


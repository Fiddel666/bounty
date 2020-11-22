import requests
from bs4 import BeautifulSoup
import json

# json to python object converter
class user(object):
	def __init__(self, j):
		self.__dict__ = json.loads(j)

# web scraper
def scrap():
	db =['name', 'warning', 'house']

	url = "https://beta.wikiversity.org/wiki/%D7%9C%D7%99%D7%9E%D7%95%D7%93%D7%99_%D7%9E%D7%97%D7%A9%D7%91%D7%99%D7%9D_%D7%91%D7%A9%D7%99%D7%98%D7%AA_%D7%91%D7%98%D7%90#%D7%A0%D7%99%D7%A0%D7%92'%D7%95%D7%AA"
	page = requests.get(url)
	#print(page.content)
	
	# creating beautiful soup instance
	soup = BeautifulSoup(page.content, 'html.parser')
	#print(soup)
	
	table = soup.find('span', id="נינג'ות")
	users = []
	for i in range(5):
		table = table.find_next('table')
		#print(i, "--------------------------------------------------")
		
		for tr in table.find_all('tr')[1:]:
			td = tr.find_all('td')
			#print(td[1].text, td[-1].a.get('title'), td[-2].text)
		
			if(i<=1):
				warning = td[-2].text.rstrip()
			else:
				warning = "0"
			if(i<=2):
				name = td[1].text.rstrip()
			else:
				name = td[0].text.rstrip()
			house = td[-1].a.get('title').rstrip() if td[-1].a else "null"
			
			values = [name, warning, house]
		
			j = "{"
			for key, val in zip(db, values):
				j += '"' + key + '"' + ': ' + '"' + val + '", '
			j = j[:-2] + "}"
			#print(j)
			usr = user(j)
			users.append(usr)
	
	return users

#scrap()


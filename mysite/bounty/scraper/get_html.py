import requests
from bs4 import BeautifulSoup
import json
#from .models import users

class user(object):
	def __init__(self, j):
		self.__dict__ = json.loads(j)
	
def scrap():
	db =[	'id', 'name', 'rank', 
			'main_topic', 'main_topic_score', 
			'secondery_topic1', 'secondery_topic1_score', 
			'secondery_topic2', 'secondery_topic2_score', 
			'warning', 'house'
		]

	url = "https://beta.wikiversity.org/wiki/%D7%9C%D7%99%D7%9E%D7%95%D7%93%D7%99_%D7%9E%D7%97%D7%A9%D7%91%D7%99%D7%9D_%D7%91%D7%A9%D7%99%D7%98%D7%AA_%D7%91%D7%98%D7%90#%D7%A0%D7%99%D7%A0%D7%92'%D7%95%D7%AA"
	page = requests.get(url)

	soup = BeautifulSoup(page.content, 'html.parser')

	tables = soup.find_all('table', class_="wikitable sortable")
	table = tables[0]
	rows = table.find_all('td')

	usrs = []
	rows_num = len(rows) // len(db)
	for usr in range(rows_num):
		j = '{'
	
		for row, var in zip(rows[usr*11::], db):
			row_elem = row.text
			#print(row_elem)
			#print(row_elem.split())
			#print('"' + var + '"' + ': ' + '"' + ''.join(row_elem.split()) + '", ')
			j += '"' + var + '"' + ': ' + '"' + ''.join(row_elem.split()) + '", '
			#print(user_obj.var)
			#print('--------------')
		
		j = j[:-2] + '}'
		#print(j)
		usr = user(j)
		usrs.append(usr)
		#print('-----end-----')

	#for usr in usrs:
		#u = users(user=usr.name, level=0, belt='transparent', house='test', status='active', warning=usr.warning)
		#u.save()
		#print(usr.id, usr.name)
	
	return usrs




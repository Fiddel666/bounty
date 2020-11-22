import requests
from bs4 import BeautifulSoup


# web scraper
def scrap():
	url = "https://beta.wikiversity.org/wiki/User:The_duke/solved_beta_challenges"
	page = requests.get(url)
	#print(page.content)
	
	# creating beautiful soup instance
	soup = BeautifulSoup(page.content, 'html.parser')
	#print(soup)
	
	scores = {}
	category = soup.find_all('span', class_="mw-headline")
	for cat in category[1:17]:
		cat.string = cat.text.replace("אתגרים", "").replace("אתגרי", "").lstrip()
		if(cat.text == "Reversing & Pwning" or cat.text == "Security"):
			continue
		#print(cat.text, "---------------------------------")
		scores[cat.string] = {}
		
		table = cat.find_next("table")
		#print(table.text)
		
		for tr in table.find_all("tr")[1:]:
			#print(tr.text)
			chall = tr.td
			#print(chall.text.rstrip())
			
			users = chall.find_next("pre")
			user = []
			
			for usr in users.text.split("*")[1:]:
				usr = usr.lstrip().rstrip()
				user.append(usr) if (" " in usr) == False else []#print(usr)
			#print(chall.text.rstrip(), user)
			
			scores[cat.string][chall.text.rstrip()] = user
			
	#for cat in scores:
	#	print(scores[cat])
	#	print("----------------------------")
	
	return scores
	
#scrap()












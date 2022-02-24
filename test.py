# this is a page for testing different functions

from bs4 import BeautifulSoup	
import requests

source = requests.get("https://realm-grinder.fandom.com/wiki/Research").text
soup = BeautifulSoup(source, "lxml")

def researchDesc(table):

	for upgrade in table.find_all('table'):
		# print(upgrade.text.strip())
		row = upgrade.find_all('tr')
		for item in row:
			if item == '\n' or '\t' in item:
				continue
			else:
				itemText = item.text.strip()

				for br in item.find_all('br'):
					br.extract()

				for p in item.find_all('p'):
					pItem = p.extract().text.strip()
					#itemText = itemText + pItem

			#print(item)
			#print(item.text.strip(), end='')
			#print("{:<30}".format(itemText, end=''))
			print("{:<30}".format(itemText.rstrip("\n"), end=''))


facility = ["Spellcraft", "Craftsmanship", "Divine_Facility", "Economics", "Alchemy", "Warfare"]

for fac in range(0, len(facility)-1):
	# finds tables with respected facilities
	facTable = soup.find('table', id=facility[fac])
	researchDesc(facTable)

# x = 0
# RPproduction = float(350 * x * 350 * x^0.75)

from bs4 import BeautifulSoup	
import requests

source = requests.get("https://realm-grinder.fandom.com/wiki/Research").text
soup = BeautifulSoup(source, "lxml")

allTable = soup.find_all('table')

facility = ["Spellcraft", "Craftsmanship", "Divine_Facility", "Economics", "Alchemy", "Warfare"]

for fac in range(0, len(facility)-1):
	# finds tables with respected facilities
	facTable = soup.find('table', id=facility[fac])
	#print(facTable.text.strip())


	# there are 3 tables for the ugprade tier
	upgradeTier = facTable.find_all('table')
	for upgrade in upgradeTier:
		# print(upgrade.text.strip())
		row = upgrade.find_all('tr')
		itemList = []
		for item in row:
			if item == '\n' or '\t' in item:
				continue
			itemText = item.text.strip()

			for br in item.find_all('br'):
				br.extract()

			for p in item.find_all('p'):
				pItem = p.extract().text.strip()
				#itemText = itemText + pItem

			itemList.append(itemText)
			#print(item)
			#print(item.text.strip(), end='')
			#print("{:<30}".format(itemText, end=''))
			print("{:<30}".format(itemText.rstrip("\n"), end=''))

		#for i in itemList:
		#	i = i.strip()
		#	print(i)
		#print(itemList)
		print("\n\n\n")
	



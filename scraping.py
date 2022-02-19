from bs4 import BeautifulSoup
import requests

source = requests.get("https://realm-grinder.fandom.com/wiki/Trophies#Tips").text
soup = BeautifulSoup(source, 'lxml')

all_table = soup.find_all('table')

buildings = ["Farms", "Inns", "Blacksmiths", "Warrior Barracks", "Knights Jousts", "Wizard Towers", "Cathedrals",
             "Citadels", "Royal Castles", "Heaven's Gates", "Slave Pens", "Orcish Arenas",
             "Witch Conclaves", "Dark Temples", "Necropolises", "Evil Fortresses", "Hell Portals",
             "Deep Mines", "Stone Pillars", "Alchemist Labs", "Monasteries", "Labyrinths", "Iron Strongholds",
             "Ancient Pyramids", "Halls of Legends"]

def print_table(table):
    print(table.th.text.strip())
    print("{:<40}{}".format("Name", "Unlock Requirement"))
    for i in range(0, 58):
        print("-", end='')
    print()
    for row in table.find_all('tr'):

        for item in row.find_all('th', recursive=False):
            itemText = item.text.strip()

            # remove breaks
            for e in item.find_all('br'):
                e.extract()
            # remove paragraphs
            for i in item.find_all('p'):
                PA = i.extract().text.strip()
                itemText = item.text.strip() + PA
            # remove paragraphs in <td>
            for desc in row.find_all('td'):
                for g in desc.find_all('p'):
                    description = g.extract().text.strip()

            if itemText != '':
                try:
                    print("{:<40}{}".format(itemText, row.td.text.strip()))
                except Exception as e:
                    if table.tr.text.strip() in buildings:
                        c = 0
                        for e in table.find_all('tr'):
                            for z in e.find_all('td'):
                                #print(z)
                                try:
                                    if len(z.text.strip()) != 0:
                                        print("{:<40}".format(z.text.strip()), end='')
                                        # print(z.extract())
                                except:
                                    pass
                            print()
                        break


                    pass

    print("\n")



for t in all_table:
    print_table(t)

#print(soup.find('table',id=buildings[0]).th.text)


#print(onlybuild.text.strip(), end='')

# print(row.text.strip(), end='')
'''onlybuild = soup.find('table', id='Farms')
for e in onlybuild.find_all('tr'):
    for g in e.find_all('td'):
        print("{:<40}".format(g.text.strip()), end='')
    print()'''



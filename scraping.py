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

# printing of a single table
def print_table(table):

    # for all building trophies
    for build in table.find_all('table'):
        print(build.th.text.strip())
        print("{:<40}{}".format("Name", "Unlock Requirement"))
        for i in range(0, 58):
            print("-", end='')
        print()
        if build.tr.text.strip() in buildings:
            for e in build.find_all('tr'):
                count = False
                for z in e.find_all('td'):
                    if len(z.text.strip()) != 0:
                        
                        print("{:<40}".format(z.text.strip()), end='')
                        count = True
                
                if count:
                    print()
            print("\n")

    # for all trophies other than building trophies
    if table.th.text.strip() not in buildings and table.th.text.strip() != "Building Types - 25x22 Trophies":
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

                    # for building trophies since it is a nested list
                    except Exception as e:
                        pass
    else:
        return


    print("\n")


for t in range(1, len(all_table)-2):
    print_table(all_table[t])






import math

# 250000 per trophy for Halls of Legends


class Faction:

    # bldList states the amount of buildings there is for each building type
    def __init__(self, reincarnation, bldList, trophy):
        self.reincarnation = reincarnation
        self.bldList = bldList
        self.trophy = trophy

        self.buildCostList = [10, 125, 600, 1800, 5600, 38000, 442000, 7300000, 145*math.pow(10, 6), 3.2*math.pow(10, 9), 200*pow(10, 9)]
        self.buildBasePdn = [2, 6, 20, 65, 200, 650, 2000, 8500, 100000, 1200000, 250000 * self.trophy]

    def call_of_arms(self):
        call = 0.3 * math.pow(self.bldAmt, 0.975) * 0.01
        return call

    # get ascension levels based on amount of reincarnations
    def get_ascension(self):
        ascension = 0
        if self.reincarnation >= 100:
            ascension = 2
        elif self.reincarnation >= 40:
            ascension = 1
        else:
            pass

        return ascension

    def spiritual_surge(self):
        return math.pow((10000 * math.pow(1.05, self.reincarnation)), (1+0.5*self.get_ascension())) * 0.01

    def building_list(self):
        bldingList = []
        nameList = ["Farm", "Inn", "Blacksmith"]
        buildCostList = [10, 125, 600]
        buildBasePdn = [2, 6, 20]
        for i in nameList:
            bldingList.append([nameList, buildCostList, buildBasePdn])
        return bldingList

        
class Good(Faction):
    def __init__(self, reincarnation, bldList, trophy):
        super().__init__(reincarnation, bldList, trophy)
        self.nameList = ["Farm", "Inn", "Blacksmith", "Warrior Barracks", "Knight Jousts", "Wizard Tower", "Cathedral", "Citadel", "Royal Castle", "Heaven's Gate", "Hall of Legends"]

    # clicking reward
    def holy_light(self):
        return 2500 * 1/100

    def get_blding_list(self):
        bldingList = [] 
        
        for i in range(0, len(self.nameList)):
            bldingList.append([self.nameList[i], self.buildCostList[i], self.buildBasePdn[i]])
            print(bldingList[i])
        
        return bldingList

class Evil(Faction):
    def __init__(self, reincarnation, bldList, trophy):
        super().__init__(reincarnation, bldList, trophy)
        self.nameList = ["Farm", "Inn", "Blacksmith", "Slave Pen", "Orcish Arena", "Witch Conclave", "Dark Temple", "Necropolis", "Evil Fortress", "Hell Portal", "Hall of Legends"]

    # production reward
    def blood_frenzy(self):
        return 1000 * 1/100

    def get_blding_list(self):
        bldingList = []
        
        for i in range(0, len(nameList)):
            bldingList.append([self.nameList[i], self.buildCostList[i], self.buildBasePdn[i]])
            print(bldingList[i])
        
        return bldingList

class Neutral(Faction):
    def __init__(self, reincarnation, bldList, trophy):
        super().__init__(reincarnation, bldList, trophy)
        self.nameList = ["Farm", "Inn", "Blacksmith", "Deep Mine", "Stone Pillars", "Alchemist Lab", "Monastery", "Labyrinth", "Iron Stronghold", "Ancient Pyramid", "Hall of Legends"]

    # increase production bonus from gems
    def gem_grinder(self):
        return 5000 * 1/100

    def get_blding_list(self):
        bldingList = []
        for i in range(0, len(nameList)):
            bldingList.append([self.nameList[i], self.buildCostList[i], self.buildBasePdn[i]])
            print(bldingList[i])



class Fairy(Good):
    def __init__(self, reincarnation, bldList, trophy):
        super().__init__(reincarnation, bldList, trophy)

    # increase production of Farms, Inns and Blacksmiths only
    def fairy_chanting(self):
        return 50000 * 1/100



#fac1 = Faction(50, "black", "fairy", 1000)
fac2 = Good(20, 2000, 500)
fac2.get_blding_list()




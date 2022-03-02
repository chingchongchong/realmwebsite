import math
from faction import Faction
from faction import Good


class Fairy(Good):
    def __init__(self, reincarnation, bldList, mana, manaRegen, trophy):
        super().__init__(reincarnation, bldList, mana, manaRegen, trophy)

    # increase production of Farms, Inns and Blacksmiths only
    def fairy_chanting(self):
        return 50000 * 1/100


    # FIRST TIER UPGRADES
    # Increase the base production of Farms by +98 and reduce the building cost multiplier.
    def pixie_dust_fertilizer(self):
        self.buildAddPdn[0] += 98 
        return self.buildAddPdn[0]

    # Increase the production of Farms, Inns and Blacksmiths by 10.000%
    def fairy_worker(self):
        list = []
        self.buildAddPdn[0] *= 100
        self.buildAddPdn[1] *= 100
        self.buildAddPdn[2] *= 100
        for i in range(0, 2):
            list.append(self.buildAddPdn[i])
        return list

    # Increases maximum Mana by the amount of Good buildings you own.
    def kind_hearts(self):
        self.mana += 1.3 * math.pow(self.mana, 0.7)
        return self.mana


    # SECOND TIER UPGRADES
    # Increase the base production of Inns by +234 and reduce the building cost multiplier.
    def fairy_cuisine(self):
        self.bldingList[1][2] += 234
        return self.bldingList[1][2]

    # Additively increase clicking reward by 20% of the production of Farms, Inns and Blacksmiths combined.
    #def golden_pots(self):






# reincarnation, amt of buildings, trophy
#fac1 = Faction(50, "black", "fairy", 1000)
fac2 = Evil(20, 2000, 500, 1000, 200)
fac2.get_blding_list()


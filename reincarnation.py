from bs4 import BeautifulSoup	
import requests
import numpy as np
import math

source = requests.get("https://realm-grinder.fandom.com/wiki/Reincarnation").text
soup = BeautifulSoup(source, "lxml")

rPower = 0

def reincarnationLvl(level):

    # these are bonuses given right at level 1
    time = 0
    productionCost = .25 * level + 1
    offProduction = 5 * level + 1           # offline production
    coinChance = .01 * level + 1
    manaRegen = 1 + math.floor((6.25 * (math.sqrt(1 + 8 * level)) - 1)/10)

    # these are following variables that come with respectively levels
    gemBonus = 0
    asstAmt = 0
    asstPdn = 0
    bldingPdn = 1
    mana = 0
    buildingProd = 0
    royalExBonus = 0    
    unqBuilding = 0
    mana2 = 0
    facFactionCoin = 0
    asstAmt2 = 0
    researchSlot = False
    manaRegen2 = 1
    unqBuildingDiff = False
    facFactionCoin2 = 1

    # increase gem bonus
    if level >=2 :
        gemBonus = level * .0002

    # increase assistant production
    if level >= 5:
        asstAmt = level * 1
        first = 0.05
        second = 0.1

        if level == 5:
            asstPdn = level * 0.02 + first + 1
        else:
            asstPdn = level * 0.02 + second + 1

    # increase building production
    if level >= 10:
        bldingPdn = 1 + math.pow(level, 1.75) * math.pow(time, 0.65)
        
    # increase max mana
    if level >= 12:
        mana = level * 35

    # increase production of each building of the same type
    if level >= 20:
        buildingProd = 1 + 0.01 * level

    # increase royal exchange bonus by 0.5% per reincarnation
    if level >= 25:
        royalExBonus = 1+ level * 0.005

    # increase production of unique buildings based on amt of reincarnation
    if level >= 41:
        unqBuilding = 1200 * (math.pow(level, 1.1))/100

    # increase max mana based on amt of reincarnation
    if level >= 45:
        mana2 = 70 * math.pow(level, 1.2)

    # multiplicatively increase faction coin find chance
    if level >= 50:
        print("", end='')

    # increase faction coins found that match your Faction or Bloodline
    if level >= 60:
        facFactionCoin = 1.2 * level

    # gain 4 additional Assistants per reincarnation (starts at 425)
    if level >= 85:
        asstAmt2 = 4 * level + 425

    if level >= 90:
        researchSlot = True

    if level >= 100:
        manaRegen2 = 1 + level * 0.01 

    # increase the production of unique buildings based on the difference of time spent
    # as their respective faction against your most used faction in this reincarnation
    if level >= 108:
        unqBuildingDiff = False

    # increase FC chance multiplicatively if they match your Faction or Bloodline or Artifact set
    if level >= 115:
        facFactionCoin2 = 1.2 * math.pow(level, 1.05)

    totalProduction = productionCost * bldingPdn
    totalUnqBuilding = unqBuilding
    totalOffPdn = offProduction
    totalCoinChance = coinChance 
    totalAssistant = asstAmt + asstAmt2
    totalAssistantPdn = asstPdn
    totalMana = mana + mana2
    totalManaRegen = manaRegen * manaRegen2
    
    totalSameFacCoin = facFactionCoin * facFactionCoin2
    buildingProd # increase production of each building of the same type

    rList = [totalProduction, totalUnqBuilding, totalOffPdn, gemBonus, totalCoinChance, totalAssistant,
             totalAssistantPdn, totalMana, totalManaRegen, royalExBonus, researchSlot, unqBuildingDiff,
             totalSameFacCoin, buildingProd]

    rNameList = ["Total Production", "Total Unique Building Production", "Total Offline Production", "Total Gem Bonus",
                 "Total Faction Coin Find Chance", "Total Additional Assistants", "Total Assistant Production",
                 "Total Mana", "Total Mana Regeneration", "Royal Exchange Bonus", "Research Slot",
                 "Unique Against Building", "Total Same Faction//Bloodline Coin Chance", "Production of Each Building Type"]

    for i in range(0, len(rList)-1):
        print("{:50}{:.2f}".format(rNameList[i], rList[i]))

    return rList


playing = True
while playing:
    try:
        rLevel = int(input("Please key in your Reincarnation Level: "))
        reincarnationLvl(rLevel)
        print()

        validation = True
        while validation:
            value = input("Do you still wish to continue? (Y/N)")
            if value.upper() == "Y":
                validation = False
            elif value.upper() == "N":
                print("Thank you for playing!")
                validation = False
                playing = False
            else:
                print("You have entered the wrong input. Please try again.")

    except Exception as e:
        print("You did not key in the values properly. Please try again.")







        
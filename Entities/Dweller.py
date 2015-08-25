import numpy as np

class Dweller:
    def __init__(self, _data):
        self.data = _data

    def getIds(self):
        tab = []
        for idx, dweller in enumerate(self.data["dwellers"]["dwellers"]):
            tab.append(dweller["serializeId"])
        return tab

    def getName(self, id):
        name = self.data["dwellers"]["dwellers"][id-1]["name"]
        return name

    def getLastName(self, id):
        lastname = self.data["dwellers"]["dwellers"][id-1]["lastname"]
        return lastname

    def getHapiness(self, id):
        happiness = self.data["dwellers"]["dwellers"][id-1]["happiness"]["happinessValue"]
        return happiness

    def getHealth(self, id):
        health = self.data["dwellers"]["dwellers"][id-1]["health"]["healthValue"]
        return health

    def getMaxHealth(self, id):
        maxHealth = self.data["dwellers"]["dwellers"][id-1]["health"]["maxHealth"]
        return maxHealth

    def getRad(self, id):
        rad = self.data["dwellers"]["dwellers"][id-1]["health"]["radiationValue"]
        return rad

    def getLevel(self, id):
        level = self.data["dwellers"]["dwellers"][id-1]["experience"]["currentLevel"]
        return level

    def getExperience(self, id):
        experience = self.data["dwellers"]["dwellers"][id-1]["experience"]["experienceValue"]
        return experience

    def getGender(self, id):
        gender = self.data["dwellers"]["dwellers"][id-1]["gender"]
        return gender

    def getAscendant(self, id):
        ascendant = self.data["dwellers"]["dwellers"][id-1]["relations"]["ascendants"]
        return ascendant

    def getReproductible(self, _id):
        notReprod = []
        for id in self.getIds():
            if any(asce == _id for asce in self.getAscendant(id)):
                notReprod.append(self.getAscendant(id))
        notReprod = self.reOrder(notReprod, _id)
        reprod = self.getReprod(notReprod, self.getGender(_id))
        return reprod

    def getReprod(self, notReprod, gender):
        tab = []
        for id in self.getIds():
            if not any(value == id for value in notReprod):
                if self.getGender(id) != gender:
                    tab.append(id)

        return tab


    def reOrder(self, _tab, _id):
        newTab = []
        for tab in _tab:
            for item in tab:
                if item > 0 and item != _id:
                    if not any(value == item for value in newTab):
                        newTab.append(item)

        return newTab
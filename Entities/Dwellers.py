from Entities.Dweller import Dweller
from Entities.Families import Families


class Dwellers:
    def __init__(self):
        self.dwellers = {}
        self.families = Families()

    def add(self, dweller):
        self.dwellers[dweller.id] = dweller

    def showAll(self):
        for key, value in self.dwellers.items():
            print(str(value.id) + ": " + value.name + " - " + str(value.gender))

    def showAllFamilies(self):
        self.families.showAll()

    def initData(self, data):
        for idx, dweller in enumerate(data):
            newDweller = Dweller()
            newDweller.initData(dweller)
            self.add(newDweller)
            ascendant = dweller["relations"]["ascendants"]
            for idx, idDweller in enumerate(ascendant):
                if int(idDweller) > 0:
                    child = self.getDweller(idDweller)
                    if(child is not None):
                        self.families.add_member(newDweller, child)

    def getDweller(self, id):
        for idx, dwellerId in enumerate(self.dwellers):
            if self.dwellers[dwellerId].id == id:
                return self.dwellers[dwellerId]
        return None
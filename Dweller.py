class Dwellers:
    def __init__(self):
        self.dwellers = {}
        
    def add(self, dweller):
        self.dwellers[dweller.id] = dweller
        
    def showAll(self):
        for key, value in self.dwellers.items():
            print(str(value.id) + ": " + value.name)
        
class Dweller:
    def __init__(self):
        self.id = None
        self._name = None
        self.lastname = None
        self.happiness = None
        self.health = None
        self.maxHealth = None
        self.rad = None
        self.level = None
        self.experience = None
        
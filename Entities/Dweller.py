class Dweller:
    def __init__(self):
        self.id = None
        self.name = None
        self.lastName = None
        self.happiness = None
        self.health = None
        self.maxHealth = None
        self.rad = None
        self.level = None
        self.experience = None
        self.father = None
        self.mother = None
        self.gender = None #1 - Femme, 2 - Homme

    def initData(self, data):
        self.id = data["serializeId"]
        self.name = data["name"]
        self.lastName = data["lastName"]
        self.happiness = data["happiness"]["happinessValue"]
        self.health = data["health"]["healthValue"]
        self.maxHealth = data["health"]["maxHealth"]
        self.rad = data["health"]["radiationValue"]
        self.experience = data["experience"]["experienceValue"]
        self.level = data["experience"]["currentLevel"]
        self.gender = data["gender"]
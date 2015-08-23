class Family:
    def __init__(self, dweller):
        self.members = []
        self.members.append(dweller)

    def addDweller(self, dweller):
        self.members.append(dweller)

    def containDweller(self, dweller):
        for idx, value in enumerate(self.members):
            if(value.id == dweller.id):
                return True
        return False
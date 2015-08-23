class Family:
    def __init__(self, dweller):
        self.members = []
        self.members.append(dweller)

    def addDweller(self, dweller):
        for idx, member in enumerate(self.members):
            if member.id == dweller.id:
                return
        self.members.append(dweller)

    def containDweller(self, dweller):
        for idx, value in enumerate(self.members):
            if(value.id == dweller.id):
                return True
        return False
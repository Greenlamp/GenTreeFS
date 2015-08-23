from Entities.Family import Family
class Families:
    def __init__(self):
        self.families = []

    def add_member(self, dweller, relative):
        if dweller.id == 13:
            print("test")
        if len(self.families) == 0:
            family = Family(relative)
            family.addDweller(dweller)
            self.families.append(family)
            return

        for idx, family in enumerate(self.families):
            if family.containDweller(relative):
                family.addDweller(dweller)
                return

        family = Family(relative)
        family.addDweller(dweller)
        self.families.append(family)
        return

    def showAll(self):
        for idx, family in enumerate(self.families):
            print("[", end=" ")
            for ifx, member in enumerate(family.members):
                print(member.name, end=" ")
            print("]")
from game_mechanics.Courences import Courences
class ShopKeeper:
    def __init__(self,inventory):
        self.inventory = inventory
        self.stock =[([(12,Courences.GOLD)],"Zwiększ ilość otrzymywanego złota","gold",0),([(12,Courences.GOLD)],"Zwiększ obronę","def",0),([(12,Courences.GOLD)],"Zwiększ zasięg podnoszenia przedmiotów","pickup",0),([(12,Courences.GOLD)],"Zwiększ szansę na obrażenia krytyczne","crit",0),([(44,Courences.GOLD)],"tba.","tba",1),([(56,Courences.GOLD)],"tba.","tba",1),([(99,Courences.GOLD)],"Shotgun: więcej pocisków i większa celność","shotgun",2)]
        self.bronze_offers = []
    def restock(self):
        pass

    def sell(self,i):
        for val in self.stock[i][0]:
            if self.inventory.money[val[1]] < val[0]:
                    break
        else: #for's else
            for val in self.stock[i][0]:
                self.inventory.money[val[1]] -= val[0]
            del self.stock[i]

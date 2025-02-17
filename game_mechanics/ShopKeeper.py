from game_mechanics.Courences import Courences
from random import randrange

class ShopKeeper:
    def __init__(self,inventory):
        self.inventory = inventory
        self.stock = []
        self.numer_of_offers = (3,2,1)
        self.bronze_offers = [([(12,Courences.GOLD)],"Zwiększ ilość otrzymywanego złota","gold",0), ([(12,Courences.GOLD)],"Zwiększ obronę","def",0), ([(12,Courences.GOLD)],"Zwiększ zasięg podnoszenia przedmiotów","pickup",0),([(12,Courences.GOLD)],"Zwiększ szansę na obrażenia krytyczne","crit",0)]
        self.silver_offers = [([(44,Courences.GOLD)],"Zwiększ mnożnik obrażeń krytycznych","mul",1),([(56,Courences.GOLD)],"Dodaj obrażenia kontaktowe","contact",1),]
        self.gold_offers = [([(99,Courences.GOLD)],"Shotgun: więcej pocisków i większa celność","shotgun",2),([(99,Courences.GOLD)],"Pistol: więcej pocisków","pistol",2),([(99,Courences.GOLD)],"Rifle: większa szybkostrzelność","rifle",2),([(99,Courences.GOLD)],"Laser: strzały seriami","laser",2),([(99,Courences.GOLD)],"Pickaxe: większa prędkość ataku","pickaxe",2),([(99,Courences.GOLD)],"Blowtorch: większy zasięg","blowtorch",2),([(99,Courences.GOLD)],"Chakra: większy zasięg","chakra",2), ]
    def restock(self):
        for _ in range(self.numer_of_offers[0]):
            if not self.bronze_offers or len(self.stock) > 5: break
            i = randrange(len(self.bronze_offers))
            self.stock.append(self.bronze_offers.pop(i))
        for _ in range(self.numer_of_offers[1]):
            if not self.silver_offers or len(self.stock) > 5: break
            i = randrange(len(self.silver_offers))
            self.stock.append(self.silver_offers.pop(i))
            # del self.silver_offers[i]
        for _ in range(self.numer_of_offers[2]):
            if not self.gold_offers or len(self.stock) > 5: break
            i = randrange(len(self.gold_offers))
            self.stock.append(self.gold_offers.pop(i))

    def sell(self,i):
        for val in self.stock[i][0]:
            if self.inventory.money[val[1]] < val[0]:
                break
        else: #for's else
            for val in self.stock[i][0]:
                self.inventory.money[val[1]] -= val[0]
            self.inventory.receive_upgrade(self.stock[i][2])
            del self.stock[i]

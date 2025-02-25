import Cioccolato
import random as rd 

#AUTORE: MATTIA

class Tavoletta(Cioccolato.Cioccolato):
        
    def __init__(self, tipo,percentuale,peso):
        super().__init__(tipo,percentuale)
        self.peso = peso
        self.aggiunte = rd.choice(["nocciole", "biscotti", "palline"])  
        self.num_tavolette = int(self.peso / 5)

    def produce(self):
        return (f"produciamo: {self.num_tavolette} cioccolatini con {self.aggiunte}")
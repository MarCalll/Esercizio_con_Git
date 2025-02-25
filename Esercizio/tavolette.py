import random as rd 

class Tavolette(Cioccolato):
    
    def __init__(self, peso, aggiunte):
        self.peso = peso
        self.aggiunte = aggiunte  

    def produce(self):
        num_tavolette = int(self.peso / 5)
        if self.aggiunte:
            
            aggiunta = rd.choice(["nocciole", "biscotti", "pralline"])
            descrizione = "aggiunte:" + aggiunta
        else:
            descrizione = "senza aggiunte"
        return "produciamo:" + num_tavolette +  "cioccolatini con " + descrizione
from Cioccolato import Cioccolato
import random

class Cioccolatini(Cioccolato):
    def __init__(self, ripieno):
        self.forma = random.choice(["Palla", "Uovo", "Cuore"])
        self.ripieno = ripieno

    def produce(self):
        quantita_cioccolato = {
            "Palla": 10,  
            "Uovo": 15,  
            "Cuore": 12   
        }
        
        cioccolato_usato = quantita_cioccolato[self.forma]
        
        return f"Produzione di un cioccolatino a forma di {self.forma} con ripieno di {self.ripieno}. Cioccolato usato: {cioccolato_usato} grammi."

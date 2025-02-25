from Cioccolato import Cioccolato

#AUTORE: PAOLO

class CioccolatoCaldo (Cioccolato):
    def __init__(self, tipo: str, percentuale_cacao: int, temperatura: int, densita: int): #tioi di dati
        super().__init__(tipo, percentuale_cacao)
        self.temperatura = temperatura
        self.densita = densita
        
    def produce(self): #metodo di istanza
        super(). produce()
        print(f"Temperatura: {self.temperatura}gradi, Densità: {self.densita}")

class Cioccolato:
        
    def __init__(self, tipo,percentuale):
        self.tipo = tipo
        self.percentuale = self.correzione_percentuale(percentuale)
        
    def produce(self):
        print(f"Cioccolato di tipo {self.tipo} con {self.percentuale} % di cacao")
        
    def correzione_percentuale(self,percentuale):
        if percentuale > 100:
            print("Valore troppo alto, imposto 100 di base.")
            return 100
        else:
            return percentuale
        
arabo = Cioccolato("Arabo",32)

arabo.produce()

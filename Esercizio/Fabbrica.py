import Cioccolatino
import Tavoletta
import CioccolatoCaldo

class Fabbrica:
    
    lista_cioccolato = []
    produzione=0
    
    def mostra_cioccolato(self):  
        for ele in self.lista_cioccolato:
            print(ele.produce())
    
    def produci(self):
        if self.produzione < 100:
            scelta = input("1.Cioccolatini - 2.Tavolette di cioccolato - 3. Cioccolato caldo: ")
            if scelta=="1":
                tipo = input("Scrivere tipo")
                percentuale = int(input("Scrivere percentuale"))
                ripieno = input("Scrivere ripieno")
                cioccolatini = Cioccolatino.Cioccolatino(tipo,percentuale,ripieno)
                self.lista_cioccolato.append(cioccolatini)
                self.produzione +=2
            if scelta =="2":
                tipo = input("Scrivere tipo")
                percentuale = int(input("Scrivere percentuale"))
                peso = int(input("Peso tavoletta"))
                tavoletta = Tavoletta.Tavoletta(tipo,percentuale,peso)
                self.lista_cioccolato.append(tavoletta)
                self.produzione += tavoletta.num_tavolette
            if scelta =="3":
                tipo = input("Scrivere tipo")
                percentuale = int(input("Scrivere percentuale"))
                densita = int(input("Peso cioccolato caldo"))
                temperatura = int(input("temperatura cioccolato caldo"))
                cioccolato_caldo=CioccolatoCaldo.CioccolatoCaldo(tipo,percentuale,densita,temperatura)
                self.lista_cioccolato.append(cioccolato_caldo)
                self.produzione += peso
        else:
            print("Fabbrica chiusa")
    
  
def menu(fabbrica):
    condizione = True
    while condizione:
        print("-------------| Menu |-------------")
        print("1. Produci cioccolata")
        print("2. Cioccolata prodotta")
        print("3. Produzione")
        print("4. Stop")
            
        scelta = input("Seleziona un'opzione: ")
        if scelta == "1":
            fabbrica.produci()
        elif scelta == "2":
            fabbrica.mostra_cioccolato()
        elif scelta == "3":
            print(fabbrica.produzione)
        elif scelta == "4":
            condizione = False
            print("Programma terminato.")
        else:
            print("Opzione non valida! Riprova.")
            
fab = Fabbrica()  
menu(fab)
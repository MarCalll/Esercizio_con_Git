class Fabbrica:
    
    def produci():
        pass
    
        
    def menu(self):
        condizione = True
        while condizione:
            print("-------------| Menu |-------------")
            print("1. Produci cioccolata")
            print("4. Stop")
            
            scelta = int(input("Seleziona un'opzione: "))
            if scelta == 1:
                pass
            elif scelta == 2:
                pass
            elif scelta == 3:
                pass
            elif scelta == 4:
                condizione = False
                print("Programma terminato.")
            else:
                print("Opzione non valida! Riprova.")

fab = Fabbrica()    
fab.menu()
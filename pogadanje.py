#Računalo slučajnim odabirom uzima jedan broj između 1 i 100, a Igrač ima 10 pokušaja za pogoditi taj broj.
#Pritom, prilikom svakog pokušaja, ako Igrač nije pogodio broj, treba se ispisati poruka "Vaš broj je veći od traženog broja" ako je veći
#ili "Vaš broj je manji od traženog broja" ako je manji.
#Na kraju, ako ni nakon 10 pokušaja Igrač (Vi) ne pogodi broj koji je Računalo odabralo treba se ispisati poruka "Potrošili ste sve pokušaje, traženi broj je: (broj)".
#Također, kada se pogodi broj ili prođe 10 pokušaja, Vaša aplikacija ne treba prestati s radom već treba ispisati meni:
#[1] Igraj pogađanje broja.
#[x] Izlaz
#Navedeni meni treba biti i na početku prilikom pokretanja aplikacije. Doradite/Dodajte upravljanje izuzecima po potrebi.

import random
class Pogađanje():
    def __init__(self):
        self.broj = (range(1,100))*10
        self.igrac_odabir = 0
        self.racunalo_odabir = 0
        self.igrac_bodovi= 0
        self.racunalo_bodovi = 0
        
    def display_title_bar(self):
        print("\t****************************************************")
        print("\t***  Igra - pogađanje brojeva  *********************")
        print("\t****************************************************")
    
    def get_user_choice(self):
        print("[1]Igraj pogađanje broja.")
        print("[x] izlaz")

        return input ("Što ćete odabrati:")

    def computer_odabir(self):
        self.racunalo_odabir=random.choice(range(1,100))
        print("Računalo je odabralo broj {}".format(self.racunalo_odabir))

    def unos_broja_igraca(self):
        self.unos_broja_igraca=int(input("Odaberite broj između 1 i 100:"))
        print("Igrač je odabrao broj {}".format(self.unos_broja_igraca))
    
    def igra(self):
        self.player=random.choice(self.igrac_odabir)
        self.computer=random.choice(self.racunalo_odabir)
        self.player_input=input("Unesite broj: ").lower()
    
    if self.player_input==" ":
            print("IgraČ je odabrao {}:".format(self.player))
            print("Računalo je odabralo {}:".format(self.computer))
            self.broj_odabir=self.broj_odabir+10
            print("Do sada je iskorišteno {} pokušaja".format(self.broj_odabir))
            self.player()
            self.igrac_bodovi+= self.broj_vrijednost
            self.igrac_bodovi()
            self.računalo_bodovi+= self.broj_vrijednost
            print("Igrač ima osvojenih {}".format(self.igrac_bodovi))
            print("Računalo ima osvojenih {}".format(self.racunalo_bodovi))

    if(self.racunalo_odabir<=100):
            print("Računalo je odabralo .")
            return self.get_user_choice()
        elif(self.igrac_odabir<=100):
            print("Čestitamo, pogodili ste broj.")
            return self.get_user_choice()
        elif(self.igrac_odabir>100):
            print("Vaš broj je veći od traženog broja")
            return self.get_user_choice()
        elif(self.igrac_odabir<100):
            print("Vaš broj je manji od traženog broja")
            return self.get_user_choice()
        elif(self.igrac_odabir = ''):
            print("Potrošili ste sve pokušaje, traženi broj je: ")
            return self.get_user_choice()

    def play(self):
        choice=''
        while choice!="x":
            choice=self.get_user_choice()
            broj_igrac=self.unos_broja_igraca()
            broj_racunalo=self.racunalo_odabir()
            while self.igrac_bodovi<=100 or self.racunalo_bodovi<=100:
                if choice=="1":
                    self.igra()
                elif choice=="x":
                    print("Hvala Vam na igri.")   

if __name__=="__main__":
    game=pogadanje()
    game.play()
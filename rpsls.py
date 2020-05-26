# prvo pretvorimo stringove (tekst) u brojeve i rjesavamo s modulom, a to znači (igrac1-racunaloigrac2)%5...
# ostatak 1 ili 2 - Win igrac1...3, 4- Win racunaloigrac2...0 Nerijeseno
# "rock","spock","paper","lizard","scissors" pretvoriti u sljedeće brojeve:
#
# 0 - rock
# 1 - spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random
from rpslsError import RpslsError 
class Rpsls:
    def _init_(self):
        self.player_input = None
        self.player_number = -1
        self.computer_number = -1
        self.computer_choice_name = None
        self.bodovi_covjek = ''
        self.bodovi_racunalo = '' 

    def display_title_bar(self):
        print("*****************************************************")
        print("*** Igra - rock, spock, paper, lizard or scissors ***")
        print("*****************************************************")

    def get_user_choice(self):
        print("\n")
        print("[1] Igraj rock, paper, scissors, lizard or spock.")
        print("[x] Izlaz.")
        print("\n")
        self.player_choice = int(input("Odaberite što želite napraviti: "))

    def broj_u_string(self):
        """
        pretvara brojeve (0, 1, 2, 3, 4) u nazive/tekst (rock, spock, paper, lizard, scissors)
        """
        if self.computer_number == 0:
            self.computer_choice_name = "rock"
        elif self.computer_number == 1:
            self.computer_choice_name = "spock"
        elif self.computer_number == 2:
            self.computer_choice_name = "paper"
        elif self.computer_number == 3:
            self.computer_choice_name = "lizard"
        elif self.computer_number == 4:
            self.computer_choice_name = "scissors"
        else:
            self.computer_choice_name = None
            raise RpslsError(103)
        return self.computer_choice_name
        


    def string_u_broj(self):
        """
        pretvara naziv/tekst (rock, spock, paper, lizard, scissors) u broj (0, 1, 2, 3, 4)
        """
        if self.player_input == "rock":
            self.player_number = 0
        elif self.player_input == "spock":
            self.player_number = 1
        elif self.player_input == "paper":
            self.player_number = 2
        elif self.player_input == "lizard":
            self.player_number = 3
        elif self.player_input == "scissors":
            self.player_number = 4
        else:
            self.player_number = -1
            raise RpslsError(102)
        return self.player_number

    def play(self):
        self.display_title_bar()
        self.get_user_choice()

        while (self.get_user_choice != 2):
            self.bodovi_covjek = 0
            self.bodovi_racunalo = 0

            if(self.player_choice  > 2 or self.player_choice < 1):
                raise RpslsError(101)
            else: 
                while (self.bodovi_covjek < 3 and self.bodovi_racunalo < 3):
                    self.player_input = input("Odaberite rock, spock, paper, lizard ili scissors: ").lower()
                    self.player_number = self.string_u_broj()
                    self.computer_number = random.randrange(0,5)
                    ostatak = (self.player_number - self.computer_number)%5
                    if(self.player_number == -1):
                        winner = "Greska"
                        raise RpslsError(102)
                    else: 
                        if (ostatak == 0):
                            winner = "Neriješeno"
                        elif (ostatak == 1 or ostatak == 2):
                            winner = "Vi (čovjek) pobjeđujete"
                            self.bodovi_covjek += 1
                        elif ostatak == 3 or ostatak == 4:
                            winner = "Računalo pobjeđuje"
                            self.bodovi_racunalo += 1
                        self.computer_choice_name = self.broj_u_string()

                    
                    print("Vi (čovjek) ste odabrali: {}".format(self.player_input.title()))
                    print("Računalo je odabralo: {}".format(self.computer_choice_name.title()))
                    print("------------------------------------------------")
                    print("Vi (čovjek) imate {} bodova.".format(self.bodovi_covjek))
                    print("Računalo ima {} bodova".format(self.bodovi_racunalo))
                    print("------------------------------------------------")

                if self.bodovi_covjek == 3:
                    print("Vi (čovjek) ste pobjednik!")
                    print("------------------------------------------------")
                elif self.bodovi_racunalo == 3:
                    print("Računalo je pobjednik!")
                    print("------------------------------------------------")
                    
                self.get_user_choice()
                
                if self.player_choice == 2:
                    print("Hvala Vam na igri! Pozdrav! :)")
                    

if __name__ == "__main__":
    game = Rpsls()
    game.play()
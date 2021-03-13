from eval import jokenpo
from random import choice
import time


valid_choice = False

print("Pedra")
time.sleep(0.5)
print("Papel")
time.sleep(0.5)
print("Ou Tesoura?")
time.sleep(0.5)

player_choice = str(input("Jokenpo!\n"))
machine_choice = choice(["Pedra","Papel","Tesoura"])

while valid_choice == False:
    print (f"Escolheu {player_choice}")
    print(f"Machina escolheu: {machine_choice}")


    player_choice = player_choice.lower()
    machine_choice = machine_choice.lower()

    
    if player_choice.lower() in ["pedra","papel","tesoura"]:
        valid_choice = True

print (jokenpo(player_choice, machine_choice))

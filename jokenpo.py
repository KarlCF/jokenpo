import time
from random import choice

valid_choice = False

machine_choice = choice(["Pedra","Papel","Tesoura"])

while valid_choice == False:
    print("Pedra")
    time.sleep(0.5)
    print("Papel")
    time.sleep(0.5)
    print("Ou Tesoura?")
    time.sleep(0.5)
    player_choice = str(input("Jokenpo!\n"))

    print (f"Escolheu {player_choice}")
    print(f"Machina escolheu: {machine_choice}")

    player_choice = player_choice.lower()
    machine_choice = machine_choice.lower()

    if player_choice.lower() in ["pedra","papel","tesoura"]:
        valid_choice = True

    if player_choice == machine_choice:
        print("Empate")

    elif player_choice == "papel" and machine_choice == "pedra":
        print("Venceu!")

    elif player_choice == "tesoura" and machine_choice == "papel":
        print("Venceu")

    elif player_choice == "pedra" and machine_choice == "tesoura":
        print("Venceu!")

    elif player_choice == "papel" and machine_choice == "tesoura":
        print("Perdeu")

    elif player_choice == "tesoura" and machine_choice == "pedra":
        print("Perdeu")

    elif player_choice == "pedra" and machine_choice == "papel":
        print("Perdeu")


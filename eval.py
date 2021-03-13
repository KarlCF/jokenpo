
def jokenpo (player_choice, machine_choice):

    if player_choice == machine_choice:
        return "Empate!"

    elif player_choice == "papel" and machine_choice == "pedra":
        return "Venceu!"

    elif player_choice == "tesoura" and machine_choice == "papel":
        return "Venceu!"

    elif player_choice == "pedra" and machine_choice == "tesoura":
        return "Perdeu"

    elif player_choice == "papel" and machine_choice == "tesoura":
        return "Perdeu"

    elif player_choice == "tesoura" and machine_choice == "pedra":
        return "Perdeu"

    elif player_choice == "pedra" and machine_choice == "papel":
        return "Perdeu"

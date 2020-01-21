import random

def voyante(player_roles, options, selected):
    if selected != "Personne":
        role = player_roles.get(selected)
        if options.get("VoyanteBavarde"):
            if random.randint(0, 100) <= options.get("VoyanteBavardePer"):
                text = "La voyante est bavarde !\nElle a espionné un joueur qui est " + str(role) + " !\n\nLa voyante se rendort."
            else:
                text = "La voyante n'est pas bavarde !\nElle a espionné un joueur qui est " + str(role) + " !\n\nLa voyante se rendort."
        else:
            text = "La voyante a espionné un joueur qui est " + str(role) + " !\n\nLa voyante se rendort."
    else:
        text = "La voyante se rendort."
    return text

def renard(game_info, selected):
    if selected != "Personne":
        if selected in game_info.get("Loups"):
            text = "Le renard perd son flair.\n\nLe renard se rendort."
            game_info["RenardFlair"] = False
        else:
            text = "Le renard garde son flair.\n\nLe renard se rendort."
    else:
        text = "Le renard garde son flair.\n\nLe renard se rendort."
    return text, game_info
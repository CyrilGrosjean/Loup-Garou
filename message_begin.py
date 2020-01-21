def nuit(night):
    text = "La nuit " + str(night) + " se lève !"
    return text

def role_reveil(role, game_info, roles_player):
    if role != "Loups":
        player = ""
        for i in roles_player.keys():
            if roles_player.get(i) == role:
                player = i
                break
        if player == "":
            player = "Personne"
        text = "Le/La " + str(role) + " se réveille ! (" + str(player) + ")\n"
    else:
        text = "Les loups garous se réveillent ! (" + str(game_info.get("Loups")) + ")\nIls désignent une victime pour cette nuit."
    return text
import random

# Tres personajes clases, gerrero, picaro y mago
# el jugador puede elegir un personaje o ver las estadisticas del mismo, si elgie la segunda opcion, preguntar cual quiere elegir
# el ordenador va a elegir un persionaje aleatorio entre esos tres
# estadisticas: vida, ira (en guerreros), energía (picaro), maná(mago), daño de ataque basico, dos habilidades para cada clase
# Atacar, defender o ver habilidades cuando se esté en un combate
# La defensa es un bono temporal para subir la defensa en el mismo turno, ya que cuando cese, la defensa bajara a la enterior
# El ordenador, cuando sea su turno, decide aleatoriamente si ataca, defiende o hace habilidad. Si hace habilidad, elegirla alatoriamente
# Condicion de vicotia y derrota y mostrar por consola si ha gandao el ordenador o el jugador

warrior = {
    "life": 100,
    "anger": 45,
    "basic damage attack": 8,
    "defense": 10,
    "rotatory sword hit": 15,
    "explosive attack": 22
}
print(warrior.keys())
def warrior_attack(opponents_life):
    opponents_life["life"] -= warrior["basic damage attack"]

def warrior_defend(self_life):
    self_life["life"] += warrior["defense"]

def warrior_use_hability(opponents_life, hability):
    if hability == 1:
        opponents_life["life"] -= warrior["rotatory sword hit"]
    else:
        opponents_life["life"] -= warrior["explosive attack"]

def warrior_see_statistics():
    for key, value in warrior.items():
        print("Warrior's " + key + " -> " + str(value))


killer = {
    "life": 75,
    "energy": 55,
    "basic damage attack": 12,
    "defense": 10,
    "surprise knife attack": 16,
    "flaming slice": 25
}

def killer_attack(opponents_life):
    opponents_life["life"] -= killer["basic damage attack"]

def killer_defend(self_life):
    self_life["life"] += killer["defense"]

def killer_use_hability(opponents_life, hability):
    if hability == 1:
        opponents_life["life"] -= killer["surprise knife attack"]
    else:
        opponents_life["life"] -= killer["flaming slice"]

def killer_see_statistics():
    for key, value in killer.items():
        print("Killer's " + key + " -> " + str(value))

wizard = {
    "life": 60,
    "mana": 34,
    "basic damage attack": 17,
    "defense": 10,
    "fire ball": 24,
    "gravity aplication": 29
}

def wizard_attack(opponents_life):
    opponents_life["life"] -= wizard["basic damage attack"]

def wizard_defend(self_life):
    self_life["life"] += wizard["defense"]

def wizard_use_hability(opponents_life, hability):
    if hability == 1:
        opponents_life["life"] -= wizard["fire ball"]
    else:
        opponents_life["life"] -= wizard["gravity aplication"]

def wizard_see_statistics():
    for key, value in wizard.items():
        print("Wizzard's " + key + " -> " + str(value))

# Characters tuple
characters = {
    "Warrior": warrior, 
    "Killer": killer,
    "Wizard": wizard
}

def player_time():
    print("Your turn.\nAttack (attcak), defend (defend), use hability (1/2) or see actual statistics (ss)...")
    player_battle_choice = input()

    # Different habilities are going to be used depending on the character chosen
    if player_character == "Warrior":
        if player_battle_choice == "attack":
            print("Player's warrior has used basic attack!")
            warrior_attack(characters[IA_character]) # Deduct life to oponent's life
            print("Actual IA's", IA_character, "'s life =", characters[IA_character]["life"])

        elif player_battle_choice == "defend":
            warrior_defend(warrior["life"])
        elif player_battle_choice == "ss":
            warrior_see_statistics()
        elif player_battle_choice == "1":
            warrior_use_hability(characters[IA_character]["life"], 1)
        elif player_battle_choice == "2":
            warrior_use_hability(characters[IA_character]["life"], 2)
        else:
            print("Option not valid. Choose a correct one.")

def battle_flow():
    # print("BATTLE IS ABOUT TO START!")
    r_number = random.randint(0, 1)

    global player_turn
    player_turn = None

    if r_number == 0:
        player_turn = True
    else:
        player_turn = False
    player_turn = True # Borrar esto cuando sea necesario
    if player_turn:
        player_time()

def initial_action():
    print("Characters to be chosen: Warrior (w), Killer (k), Wizard(z). Choose character or see statistics (ss)...")
    initial_player_action = input()

    # A dictionary is done to relate each answer (w, k, z, ss) to its meaning
    options = {
        "w": "Warrior",
        "k": "Killer",
        "z": "Wizard",
        "ss": "See statistics"
    }
    option_is_valid = None

    # Depending of the option chosen by the player, a boolean takes a value or another
    for i in options.keys():
        if initial_player_action != i:
            option_is_valid = False
        else:
            option_is_valid = True
            break

    # If boolean is true, comtinue with question with player and the beggining of the battle, otherwise
    # use reclusion to repeat the process until the user takes a valid choice
    if option_is_valid:
        if initial_player_action == "ss":
            print("From which character?")
            statistics_option = input()
            if statistics_option == "w":
                warrior_see_statistics()
            elif statistics_option == "k":
                killer_see_statistics()
            else:
                wizard_see_statistics()
            initial_action()
        else:
            # Player character
            global player_character
            player_character = options[initial_player_action]

            # Fo IA character, we store the keys of characters in a list for later pick a random one (a character)
            character_names = []
            for i in characters.keys():
                character_names.append(i)
            global IA_character
            IA_character = character_names[random.randint(0, 2)]

            print("Chosen character: ", player_character)

            print("IA choice: ", IA_character)
            print("BATTLE IS ABOUT TO START!")
            battle_flow()
    else:
        print("Chosen option not valid.")
        initial_action()

initial_action()


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

killer = {
    "life": 75,
    "energy": 55,
    "basic damage attack": 12,
    "defense": 10,
    "surprise knife attack": 16,
    "flaming slice": 25
}

wizard = {
    "life": 60,
    "mana": 34,
    "basic damage attack": 17,
    "defense": 10,
    "fire ball": 24,
    "gravity aplication": 29
}

def attack(player_ch, AI_ch):
    if player_turn:
        print("Player's", player_character, "has used basic attack!")
        AI_ch["life"] -= player_ch["basic damage attack"]
        print("Actual IA's life =", characters[IA_character]["life"])
    else:
        print("AI's", IA_character, "has used basic attack!")
        player_ch["life"] -= AI_ch["basic damage attack"]
        print("Actual Player's life =", characters[player_character]["life"])
    
def defend(player_ch, AI_ch):
    if player_turn:
        print("Player's ", player_character, "life has incremented temporally during this round!")
        player_ch["life"] += player_ch["defense"]
        print("Actual Player's life: ", player_ch["life"])
    else:
        print("AI's ", IA_character, "life has incremented temporally during this round!")
        AI_ch["life"] += AI_ch["defense"]
        print("Actual AI's life: ", AI_ch["life"])

def use_hability(player_ch, AI_ch, hability):
    counter = 0
    
    if player_turn:
        if hability == 1:
            for i in player_ch.keys(): #  We need to work with exactly 1 of 2 habilites that characters have, so we use a 'for' and a counter to work  with the correct hability
                if counter == 5:
                    print("Player has used", i)
                    AI_ch["life"] -= player_ch[i]
                    print("Actual AI's life:", AI_ch["life"])
                    break
                counter += 1
            
        else:
            for i in player_ch.keys():
                if counter == 6:
                    print("Player has used", i)
                    AI_ch["life"] -= player_ch[i]
                    print("Actual AI's life:", AI_ch["life"])
                counter += 1
    
    else:
        if hability == 1:
            for i in AI_ch.keys():
                if counter == 5:
                    print("AI has used", i)
                    player_ch["life"] -= AI_ch[i]
                    print("Actual Player's life:", player_ch["life"])
                    break
                counter += 1
            
        else:
            for i in player_ch.keys():
                if counter == 6:
                    print("AI has used", i)
                    player_ch["life"] -= AI_ch[i]
                    print("Actual Player's life:", player_ch["life"])
                counter += 1

def see_statistics(player_ch):
    if player_ch == warrior:
        for key, value in player_ch.items():
            print("Warrior's", key, "->", value)
    elif player_ch == killer:
        for key, value in player_ch.items():
            print("Killer's", key, "->", value)
    else:
        for key, value in player_ch.items():
            print("Wizard's", key, "->", value)

# Characters tuple
characters = {
    "Warrior": warrior, 
    "Killer": killer,
    "Wizard": wizard
}

def turns(turn):
    battle_choice = None
    if turn:
        print("Your turn.\nAttack (attack), defend (defend), use hability (1/2) or see actual statistics (ss)...")
        battle_choice = input()
    else:
        print("AI's turn.")
        options = ["attack", "defend", "1", "2"]
        battle_choice = options[random.randint(0, 3)]
        print(battle_choice)

    # Different habilities are going to be used depending on the character chosen
    if battle_choice == "attack":
        attack(characters[player_character], characters[IA_character])
    elif battle_choice == "defend":
        defend(characters[player_character], characters[IA_character])
    elif battle_choice == "ss":
        see_statistics(characters[player_character])
    elif battle_choice == "1":
        use_hability(characters[player_character], characters[IA_character], 1)
    elif battle_choice == "2":
        use_hability(characters[player_character], characters[IA_character], 2)
    else:
        print("Option not valid. Choose a correct one.")
        turns()
    
    

def battle_flow():
    # print("BATTLE IS ABOUT TO START!")
    global player_turn
    player_turn = None
    r_number = random.randint(0, 1)

    if r_number == 0:
        player_turn = True
    else:
        player_turn = False
    #player_turn = True # Borrar esto cuando sea necesario
    while True:
        turns(player_turn)
        if player_turn:
            player_turn = False
        else:
            player_turn = True

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
            see_statistics(characters[options[statistics_option]]) # Use 2 dictionaries in order to get to the statistics
            initial_action()
        else:
            # Player character
            global player_character
            player_character = options[initial_player_action]

            # For IA character, we store the keys of characters in a list for later pick a random one (a character) and assign the character to the AI
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



import sys
import os
import time
import random
import pygame

level = 1
max_hp = 150
max_sp = 100
medicine = 2
snuff_soul = 2
chosen_persona = None
hp = max_hp
sp = max_sp
persona_name = ""
tarukaja_active = False
persona_evolved = False

def choose_persona_options():
    global chosen_persona
    while True:
        persona = input("->")
        if persona.lower() == "izanagi":
            input("Igor - Ah, Izanagi. A very wise choice.")
            chosen_persona = "izanagi"
            break
        elif persona.lower() == "orpheus":
            input("Igor - Ah, Orpheus. A very wise choice.")
            chosen_persona = "orpheus"
            break
        else:
            print("Command not valid.")

def choose_persona():
    global persona_name
    pygame.mixer.init()
    pygame.mixer.music.load('velvet room.mp3')
    pygame.mixer.music.play()
    input("Long nosed man - Welcome to the Velvet Room")
    input("Long nosed man - My name is Igor")    
    input("Igor - You will face a journey.")
    input("Igor - A journey that is filled with peril")
    input("Igor - Allow me to show you 2 fine personas")
    input("Igor - Here we have Izanagi and Orpheus")
    input("Igor - They have their strengths and weaknesses")
    
    print("############################################")
    print("      Izanagi        #        Orpheus       ")
    print("############################################")
    print("     Speed = 3               Speed = 1      ")
    print("  Phys damage =  //      Phys damage = //// ")
    print("  Magic damage = ///    Magic damage = ///  ")
    print("############################################")
    print("Please take your time and make a selection.")
    choose_persona_options()
    pygame.mixer.music.stop()

def dodge_check(dodge_chance):
    return random.randint(1, 10) <= dodge_chance

def start_game():
    global chosen_persona
    print("Please enter a name")
    name = input("->")
    time.sleep(1)
    print("Welcome", name)
    time.sleep(1)
    print("Starting game...")
    choose_persona()
    enter_tartarus()

def title_screen_options():
    option = input("->")
    if option.lower() == "play":
        start_game()
    elif option.lower() == "help":
        help_menu()
    elif option.lower() == "quit":
        pygame.mixer.music.stop()
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("Command not valid.")
        option = input("->")
        if option.lower() == "play":
            pygame.mixer.music.stop()
            start_game()
        elif option.lower() == "help":
            help_menu()
        elif option.lower() == "quit":
            pygame.mixer.music.stop()
            sys.exit()

def title_screen():
    os.system('clear')
    pygame.mixer.init()
    pygame.mixer.music.load('p4 menu.mp3')
    pygame.mixer.music.play()
    print('###############################')
    print('# Welcome to Persona GoldLoad #')
    print('###############################')
    print('#            -Play-           #')
    print('#                             #')
    print('#            -Help-           #')
    print('#                             #')
    print('#            -Quit-           #')
    print('###############################')
    title_screen_options()

def help_menu():
    print('###############################')
    print('# Welcome to Persona GoldLoad #')
    print('###############################')
    print('#     Explore Tartarus.       #')
    print('#     There Are 10 floors     #')
    print('#   Encounter shadows and     #')
    print('#   defeat them using your:   #')
    print('#          Persona!           #')
    print('###############################')
    title_screen_options()

def evolve_persona():
    global chosen_persona, persona_name, max_hp, max_sp, persona_evolved
    if chosen_persona == "izanagi":
        chosen_persona = "izanagi no okami"
        persona_name = "Izanagi no Okami"
        max_hp = 200
        max_sp = 150
    elif chosen_persona == "orpheus":
        chosen_persona = "orpheus telos"
        persona_name = "Orpheus Telos"
        max_hp = 250
        max_sp = 200
    persona_evolved = True
    print(f"{persona_name} has learned powerful new abilities!")

def enter_tartarus():
    global level
    for current_floor in range(1, 11):
        if current_floor == 10:
            print(f"You have reached the 10th floor. A formidable presence awaits you...")
            battle_shadows(is_boss=True)
        else:
            print(f"You are on floor {current_floor} of Tartarus.")
            input("You encounter a shadow! Prepare for battle...")
            battle_shadows()
            print(f"You move on to the next floor.\n")
            time.sleep(2)

def battle_shadows(is_boss=False, mini_boss=False):
    global hp, sp, medicine, snuff_soul, level, max_hp, max_sp, chosen_persona, persona_name, tarukaja_active, persona_evolved
    shadow_hp = random.randint(50, 70)
    if is_boss:
        shadow_hp = 500
    elif mini_boss:
        shadow_hp = random.randint(80, 100)
    print("A shadow appears! Prepare for battle.")
    
    shadow_moves = ['bash', 'agi', 'bufu', 'garu', 'zio']
    
    while shadow_hp > 0 and hp > 0:
        print(f"Your HP: {hp}/{max_hp} | Your SP: {sp}/{max_sp} | Shadow's HP: {shadow_hp}")
        action = input("Choose your action: Attack (a), Persona (p), Heal (h), Use Medicine (m), or Use Snuff Soul (s): ")

        dodge_chance = 0
        if chosen_persona == "izanagi":
            dodge_chance = 3
        elif chosen_persona == "orpheus":
            dodge_chance = 1
        
        shadow_dodge = dodge_check(2)
        
        if action.lower() == "a" and not shadow_dodge:
            damage = random.randint(20, 30) + level * 2
            if tarukaja_active:
                damage *= 2
                print("Tarukaja is active! Damage is doubled.")
            shadow_hp -= damage
            print(f"You dealt {damage} damage to the shadow.")
            tarukaja_active = False
        elif action.lower() == "p" and not shadow_dodge:
            if chosen_persona == "izanagi":
                if persona_evolved:
                    skill = input("Choose skill: Ziodyne (z), God Hand (b), or Ultikaja (t): ")
                    if skill.lower() == "z":
                        damage = random.randint(80, 120) + level * 2
                        shadow_hp -= damage
                        sp -= 20
                        print(f"Ziodyne dealt {damage} damage to the shadow.")
                    elif skill.lower() == "b":
                        damage = random.randint(80, 120) + level * 2
                        shadow_hp -= damage
                        hp -= 5
                        print(f"God Hand dealt {damage} damage to the shadow.")
                    elif skill.lower() == "t":
                        tarukaja_active = True
                        sp -= 10
                        print("Ultikaja! The next attack will be tripled in damage.")
                else:
                    skill = input("Choose skill: Zio (z), Bash (b), or Tarukaja (t): ")
                    if skill.lower() == "z":
                        damage = random.randint(30, 50) + level * 2
                        shadow_hp -= damage
                        sp -= 10
                        print(f"Zio dealt {damage} damage to the shadow.")
                    elif skill.lower() == "b":
                        damage = random.randint(30, 50) + level * 2
                        shadow_hp -= damage
                        hp -= 5
                        print(f"Bash dealt {damage} damage to the shadow.")
                    elif skill.lower() == "t":
                        tarukaja_active = True
                        sp -= 10
                        print("Tarukaja is active! Next attack will deal double damage.")
            
            elif chosen_persona == "orpheus":
                if persona_evolved:
                    skill = input("Choose skill: Burning Petals (a), God Hand (b), or Salvation (d): ")
                    if skill.lower() == "a":
                        damage = random.randint(50, 70) + level * 2
                        shadow_hp -= damage
                        sp -= 20
                        print(f"Burning Petals dealt {damage} damage to the shadow.")
                    elif skill.lower() == "b":
                        damage = random.randint(40, 60) + level * 2
                        shadow_hp -= damage
                        hp -= 5
                        print(f"God Hand dealt {damage} damage to the shadow.")
                    elif skill.lower() == "d":
                        hp = max_hp
                        sp -= 20
                        print("Salvation fully healed you!")
                else:
                    skill = input("Choose skill: Agi (a), Bash (b), or Dia (d): ")
                    if skill.lower() == "a":
                        damage = random.randint(30, 50) + level * 2
                        shadow_hp -= damage
                        sp -= 10
                        print(f"Agi dealt {damage} damage to the shadow.")
                    elif skill.lower() == "b":
                        damage = random.randint(30, 50) + level * 2
                        shadow_hp -= damage
                        hp -= 5
                        print(f"Bash dealt {damage} damage to the shadow.")
                    elif skill.lower() == "d":
                        hp = min(max_hp, hp + max_hp // 2)
                        sp -= 10
                        print(f"Dia healed you for {max_hp // 2} HP.")
        
        elif action.lower() == "m" and medicine > 0:
            hp = min(max_hp, hp + 100)
            medicine -= 1
            print(f"You used a Medicine. Your HP is now {hp}. You have {medicine} Medicine(s) left.")
        elif action.lower() == "s" and snuff_soul > 0:
            sp = min(max_sp, sp + 50)
            snuff_soul -= 1
            print(f"You used a Snuff Soul. Your SP is now {sp}. You have {snuff_soul} Snuff Soul(s) left.")
        
        if not dodge_check(2):
            shadow_move = random.choice(shadow_moves)
            if shadow_move == 'bash':
                damage = random.randint(10, 15)
                hp -= damage
                print(f"The shadow used Bash and dealt {damage} damage to you!")
            elif shadow_move == 'agi':
                damage = random.randint(15, 20)
                hp -= damage
                print(f"The shadow used Agi and dealt {damage} damage to you!")
            elif shadow_move == 'bufu':
                damage = random.randint(15, 20)
                hp -= damage
                print(f"The shadow used Bufu and dealt {damage} damage to you!")
            elif shadow_move == 'garu':
                damage = random.randint(15, 20)
                hp -= damage
                print(f"The shadow used Garu and dealt {damage} damage to you!")
            elif shadow_move == 'zio':
                damage = random.randint(15, 20)
                hp -= damage
                print(f"The shadow used Zio and dealt {damage} damage to you!")

        time.sleep(1)
        
    if hp <= 0:
        print("You have been defeated. Game Over.")
        sys.exit()

title_screen()


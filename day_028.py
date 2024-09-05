import random
import os
import time

#Subroutines
def health_status():
  health = (random.randint(1,6)) * (random.randint(1,12)) / 2 + 10
  return health

def strength_status():
  strength = (random.randint(1,6)) * (random.randint(1,12)) / 2 + 12
  return strength
  

def roll_dice():
   dice = random.randint(1,6)
   return dice

def calculate_damage():
    damage = abs(player_1_strength - player_2_strength) + 1
    return damage
          

print('Character builder')
print()

#player_1
player_1_name = str(input('Name Your Legend: '))
print()
player_1_valid_types = ['Human', 'Elf', 'Wizard', 'Orc']
player_1_character_type = str(input('Character Type (Human, Elf, Wizard, Orc): ')).capitalize()
while player_1_character_type not in player_1_valid_types:
    print(f'{player_1_character_type} is not valid. Please try again!')
    player_1_character_type = str(input('Character Type (Human, Elf, Wizard, Orc): ')).capitalize()
print()

#calling function for player 1
player_1_health = health_status()
player_1_strength = strength_status()

#player 1 output
print(f'{player_1_name.capitalize()}, {player_1_character_type.capitalize()}')
print('Health: ', int(player_1_health))
print( 'Strength: ', int(player_1_strength))
print()

# Player 2
player_2_name = str(input('Name Your Legend: '))
print()
player_2_valid_types = ['Human', 'Elf', 'Wizard', 'Orc']
player_2_character_type = str(input('Character Type (Human, Elf, Wizard, Orc): ')).capitalize()
while player_2_character_type not in player_2_valid_types:
    print(f'{player_2_character_type} is not valid. Please try again!')
    player_2_character_type = str(input('Character Type (Human, Elf, Wizard, Orc): ')).capitalize()
print()

#calling function for player 2
player_2_health = health_status()
player_2_strength = strength_status()

# player 2 output
print(f'{player_2_name.capitalize()}, {player_2_character_type.capitalize()}')
print('Health: ', int(player_2_health))
print( 'Strength: ', int(player_2_strength))
print()


# Rounds
rounds = 0
winner = None

#damages
player_damage = calculate_damage()


while True:
    print(' ⚔️🛡️ BATTLE TIME 🛡️⚔️')
    if rounds == 0:
        print('The battle begins!')
        time.sleep(3)
        os.system("cls")
    player_1_dice = roll_dice()
    player_2_dice = roll_dice()
    if player_1_dice > player_2_dice:
            winner = player_1_name
            print(f'{player_1_name} wins now. {player_2_name} takes a hit, with {int(player_damage)} damage 🫣 ')
            rounds = rounds + 1
            player_2_health = (player_2_health - player_damage)
            player_1_health = player_1_health
            print()

    elif player_2_dice > player_1_dice:
            winner = player_2_name
            print(f'{player_2_name} wins now. {player_1_name} takes a hit, with {int(player_damage)} damage 🆘 ')
            rounds = rounds + 1
            player_1_health = (player_1_health - player_damage)
            player_2_health = player_2_health
            print()
         
    else:
            winner = None
            print(f' {player_1_name} attacked but {player_2_name} defended well. Nobody wins')
            rounds = rounds + 1
            player_2_health = player_2_health 
            player_1_health = player_1_health
            print()
            
    print(player_1_name) 
    print(f'HEALTH: {int(player_1_health)}')  
    print()
    print(player_2_name) 
    print(f'HEALTH: {int(player_2_health)}') 
    print()
    if  player_1_health > 0 and player_2_health > 0:
        input() #input to expect an "enter" before proceed into the game
        os.system("cls")
        print('And they are both standing for the next round!')   


    if player_1_health <= 0:
        print(f'Oh no! {player_1_name} has died! {player_2_name} destroyed {player_1_name} in {rounds} rounds!')
        break
    elif player_2_health <= 0:
        print(f'Oh no! {player_2_name} has died! {player_1_name} destroyed {player_2_name} in {rounds} rounds!')
        break




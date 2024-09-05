import random
import os
import time

# Classes
class Player:
    def __init__(self, name, character_type):
        self.name = name
        self.character_type = character_type
        self.health = health_status()
        self.strength = strength_status()
    
    def define_player():
        name = str(input('Name Your Legend: '))
        print()
        valid_types = ['Human', 'Elf', 'Wizard', 'Orc']
        character_type = str(input('Character Type (Human, Elf, Wizard, Orc): ')).capitalize()
        while character_type not in valid_types:
            print(f'{character_type} is not valid. Please try again!')
            character_type = str(input('Character Type (Human, Elf, Wizard, Orc): ')).capitalize()
        print()
        return Player(name, character_type)



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
    damage = abs(player_1.strength - player_2.strength) + 1
    return damage
          

print('Character builder')
print()

#player_1
player_1 = Player.define_player()


#player 1 output
print(f'{player_1.name.capitalize()}, {player_1.character_type.capitalize()}')
print('Health: ', int(player_1.health))
print( 'Strength: ', int(player_1.strength))
print()

# Player 2
player_2 = Player.define_player()

# player 2 output
print(f'{player_2.name.capitalize()}, {player_2.character_type.capitalize()}')
print('Health: ', int(player_2.health))
print( 'Strength: ', int(player_2.strength))
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
            winner = player_1.name
            print(f'{player_1.name} wins now. {player_2.name} takes a hit, with {int(player_damage)} damage 🫣 ')
            rounds = rounds + 1
            player_2.health = (player_2.health - player_damage)
            player_1.health = player_1.health
            print()

    elif player_2_dice > player_1_dice:
            winner = player_2.name
            print(f'{player_2.name} wins now. {player_1.name} takes a hit, with {int(player_damage)} damage 🆘 ')
            rounds = rounds + 1
            player_1.health = (player_1.health - player_damage)
            player_2.health = player_2.health
            print()
         
    else:
            winner = None
            print(f' {player_1.name} attacked but {player_2.name} defended well. Nobody wins')
            rounds = rounds + 1
            player_2.health = player_2.health 
            player_1.health = player_1.health
            print()
            
    print(player_1.name) 
    print(f'HEALTH: {int(player_1.health)}')  
    print()
    print(player_2.name) 
    print(f'HEALTH: {int(player_2.health)}') 
    if  player_1.health > 0 and player_2.health > 0:
        input() #input to expect an "enter" before proceed into the game
        os.system("cls")
        print('And they are both standing for the next round!')   


    if player_1.health <= 0:
        print(f'Oh no! {player_1.name} has died! {player_2.name} destroyed {player_1.name} in {rounds} rounds!')
        break
    elif player_2.health <= 0:
        print(f'Oh no! {player_2.name} has died! {player_1.name} destroyed {player_2.name} in {rounds} rounds!')
        break




import random
import os
import time


def character_info():
  name = str(input('Name Your Legend: '))
  print()
  valid_types = ['Human', 'Elf', 'Wizard', 'Orc']
  character_type = str(input('Character Type (Human, Elf, Wizard, Orc): ')).capitalize()
  while character_type not in valid_types:
    print(f'{character_type} is not valid. Please try again!')
    character_type = str(input('Character Type (Human, Elf, Wizard, Orc): ')).capitalize()
  print()
  return name, character_type

  
def health_status():
  health = (random.randint(1,6)) * (random.randint(1,12)) / 2 + 10
  return health

def strength_status():
  strength = (random.randint(1,6)) * (random.randint(1,12)) / 2 + 12
  return strength
  
while True:

  print('Character builder')
  print()
  
  name, character_type = character_info()
  health = health_status()
  strength = strength_status()
  
  print('\033[35m',name.capitalize(),'\033[0m', ',','\033[35m',character_type.capitalize(),'\033[0m')
  time.sleep(2)
  print('Health: ','\033[31m', int(health),'\033[0m')
  time.sleep(2)
  print( 'Strength: ','\033[31m', int(strength),'\033[0m')
  print()
  print('\033[33m','May your name go down in Legend...','\033[0m')
  print()
  play_again = input('Do you want to create another character? (yes/no) ')
  if play_again.lower() == "yes":
    os.system("cls")
    continue
  else:
    print('Thanks for playing! 🎲⚔️')
    break



#Day 25/100 - Pamela Gomes
#Character Stats Generator
import random

#dices of 6 and 8 sides
def dices():
    value_six = random.randint(1,6)
    value_eight = random.randint(1,8)
    health = value_six * value_eight
    return health

#character's health
print('Character Stats Generator ⚔️🛡️')
print()
warrior_name = ""
create_another_character = "yes"

while create_another_character == 'yes':
    warrior_name = input('Name your warrior: ')
    warrior_health = dices()
    print(f"{warrior_name.title()}'s health is {warrior_health}hp.")
    print()
    create_another_character = str(input('Do you want to create another character? ')).lower()

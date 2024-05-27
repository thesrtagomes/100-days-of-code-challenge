#day 24/100 - Pamela Gomes
#Parameters
import random

print('The Infinity Dice Game 🎲🎮')
print()

def roll_dice(user_sides):
    random_sides = random.randint(1, max(user_sides, 2))
    print('You rolled ',random_sides)

user_sides = int(input('How many sides? '))

while True:
    roll_dice(user_sides)
    play_again = input('Roll again? ').lower()
    if play_again != "yes" and play_again != "y":
     break

  
  
  

  
 
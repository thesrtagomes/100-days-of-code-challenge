def animals_sound(animal):
  if animal == 'cow':
    sound = 'moo'
  elif animal == 'dog':
    sound = 'woof'
  elif animal == 'cat':
    sound = 'meow'
  else:
    sound = 'unknown'
  return sound

def play_itself ():
  animal = input('What animal would you like to hear? ').lower()
  animal_sound = animals_sound(animal)
  print()
  print(f'The {animal} goes {animal_sound}')
  print()
  
quit = ''
while quit != 'no':
    play_itself()
    quit = input('Do you want to play again? ')
print('Thank you for playing here!')








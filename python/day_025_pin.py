#Pin Picker
def pin_picker(number):
  import random
  pin = ''
  for i in range(number):
    pin += str(random.randint(0,9))
  return pin

user_number = int(input('How many numbers do you want your pin to have? '))
user_pin = pin_picker(user_number)
print(user_pin)
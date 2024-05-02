import random 
attempts = 0
number = random.randint(1,1000000)
while True:
    user_guess = int(input("Guess a number between 1 and 1,000,000: "))
    if user_guess < number and user_guess > 0:
        print('Too low. Try again.')
        attempts += 1
    elif user_guess > number:
        print('Too high. Try again.')
        attempts += 1
    elif user_guess < 0:
        exit()
    else:
        attempts += 1
        break
print(f'''Congratulations😊⭐🚀 
The number {number} is the correct number.
It took you {attempts} attempt(s). Awesome!🚀🥇''')
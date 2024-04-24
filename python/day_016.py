#Day 16 of 100: While true Loop
print('Fill in the blanck lyrics!')
print('(Type in the blanck lyrics and find out!)')
print()
counter = 0
while True:
    print('"You are my sunshine, my ______ sunshine"')
    guess = input('What word is missing? ').lower()
    counter += 1
    if guess != "only":
        print('Nops, try again')
    else:
        print(f'Congratulations! You did it. It took you {counter} attempts. WELL DONE 🚀') 
        break   
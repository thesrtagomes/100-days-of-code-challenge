from getpass import getpass as input

def ask_object():  #function to define played weapon
    object = input('Choose your weapon: R (rock 🪨), P (paper 🧻) or S (scissors ✂️) :').upper()
    if object in ['R', 'P', 'S']:
        return object
    print('Unfortunately we cannot deliver this weapon today. Try again.')
    return ask_object()

def what_wins_against(thing): #Parameters to win
    if thing == 'R':
        return 'P'
    elif thing == 'P':
        return 'S'
    elif thing == 'S':
        return 'R'
    
def emojis(object): #emojis definition
    if object == 'R':
        return '🪨'
    elif object == 'P':
        return '🧻'
    elif object == 'S':
        return '✂️'
    
player_1_victory = 0
player_2_victory = 0  

while True:
    player_1 = ask_object()
    player_2 = ask_object()
    
    print(f"{emojis(player_1)}  - {emojis(player_2)}")

    if player_1 == what_wins_against(player_2):
        print('Player 1 won 🥇')
        player_1_victory += 1
        print(f'Player 1: {player_1_victory} X Player 2: {player_2_victory}')
    
    elif player_2 == what_wins_against(player_1):
        print('Player 2 wins! ⭐')
        player_2_victory += 1
        print(f'Player 1: {player_1_victory} X Player 2: {player_2_victory}')
     
    else:
        print('Draw. Play again')
        
    if player_1_victory == 3 or player_2_victory == 3:
        break
        
print(f'Player 1 won {player_1_victory} times and Player 2 won {player_2_victory} times')
exit()
    


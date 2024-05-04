username = 'Pamela'
password = 'Ilovefrogs'

def login():
    username_input = input('What is your username? ')
    password_input = input('What is yout password? ')
    print()
    if username_input == username and password_input == password:
        print('Welcome to Replit!')
    else:
        print("Whoops! I don't recognize that username or password. Try again!")
        print()
        login()


print('Replit Login System')
print()


login()
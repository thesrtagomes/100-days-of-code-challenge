# 100 days of code: day 6
print("LOGIN SYSTEM")
print()
username = input("What is your username? ")
password = input("What is your password? ")

if (
    username == "Pamela"
    and password == "P@mela"
    or username == "Gabriel"
    and password == "G@briel"
):
    print("Welcome to the system,", username)
    if username == "Pamela":
        print("I hope you are having a great day at work today!")
    else:
        print("I hope you were able to debug that code!")
else:
    print("Incorrect username or password. Please try again.")

# DAY 5 OF 100 DAYS OF CODE
print("Marvel Movie Character Creator")
print("--")
print()
spiderman = input("Do you like 'hanging around'?: ")
if spiderman == "yes":
    print("Then you are Spider-man!")
elif spiderman == "no":
    print("Then you are not Spider-man!")
    print()
    korg = input("Do you have a 'gravelly' voice?: ")
    if korg == "yes":
        print("Then you are Korg!")
    elif korg == "no":
        print("Aww, then you are not Korg!")
        print()
        marvel = input("Do you often feel 'Marvelous'?: ")
        if marvel == "yes":
            print("Aha! You are Captain Marvel!")
        elif marvel == "no":
            print("I am sorry. I guess you are not a Marvel character.")
else:
    print("Please answer with YES or NO")

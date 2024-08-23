# 100 days of code: day 7
tv_show = input("What is your favorite TV show? ")
if tv_show == "My Demon":
    print("I love My Demon!")
    fav_character = input("What is your favorite character? ")
    if fav_character == "Do Do-Hee":
        print("I love her character too!")
    elif fav_character == "Jeong Gu-Won":
        print("He is the best player for sure.")
    else:
        print(f"Hmm, {fav_character} is a good character too.")

elif tv_show == "Tomorrow":
    print("I am watching Tomorrow with my boyfriend and I love it!")
    fav_character = input("What is your favorite character? ")
    if fav_character == "Goo Ryeon":
        print("Yes! She is perfect! She is such a great character!")
    elif fav_character == "Park Joong Gil":
        print("Oh no. He is such a pain. He is so annoying!")
    else:
        print(f"Oh, I do not like {fav_character}.")
else:
    print("I haven't watched this TV show yet. Thank you for the tip")

def colorize(text, color):
    if color == "yellow":
        print("\033[1;33m", text, sep="", end="")
    elif color == "purple":
        print("\033[1;35m", text, sep="", end="")
    elif color == "red":
        print("\033[1;31m", text, sep="", end="")
    elif color == "blue":
        print("\033[1;34m", text, sep="", end="")
    return ""


print(colorize("Super Subroutine", "yellow"))
print()
print(
    colorize("With my ", "yellow"),
    colorize("new program ", "purple"),
    colorize("I can just call red('and') ", "yellow"),
    colorize("and ", "red"),
    colorize("that word will appear in the color I set it to. ", "yellow"),
)
print()
print(colorize("With no ", "yellow"), colorize("weird gaps", "blue"))
print()
print(colorize("Epic.", "yellow"))

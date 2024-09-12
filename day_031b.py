import shutil #import para poder pegar o tamanho do terminal

def colorize(text, color):
    if color == "red":
        return f"\033[31m{text}\033[0m"
    if color == "blue":
        return f"\033[34m{text}\033[0m"
    if color == "yellow":
        return f"\033[33m{text}\033[0m"

terminal_width = shutil.get_terminal_size().columns


title = "WELCOME TO"
armbook = "--    ARMBOOK    --"  
line_1 = "Definitely not a rip off of"
line_2 = "a certain other social"
line_3 = "networking site."
honest = "Honest."

# Centralizar primeiro e depois colorir 
print(f"{title:^{terminal_width}}")
print(colorize(f"{armbook:^{terminal_width}}", "blue"))
print()
print(colorize(f"{line_1:>{terminal_width}}", "yellow"))
print(colorize(f"{line_2:>{terminal_width}}", "yellow"))
print(colorize(f"{line_3:>{terminal_width}}", "yellow"))
print()
print(colorize(f"{honest:^{terminal_width}}", "red"))
print()
print(f"{'Username:':^{terminal_width}}")
print(f"{'Password:':^{terminal_width}}")


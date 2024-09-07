def colorize(text, color):
    if color == "red":
        return f"\033[31m{text}\033[0m"
    if color == "blue":
        return f"\033[34m{text}\033[0m"
    if color == "yellow":
        return f"\033[33m{text}\033[0m"
    if color == "green":
        return f"\033[32m{text}\033[0m"
    if color == "purple": 
        return f"\033[35m{text}\033[0m"   

 
title = (colorize("=","red") +
    "=" +
    colorize("=","blue")+
    colorize( " Music App ", "yellow")+ 
    colorize("=","blue")+
    "="+
    colorize("=","red"))
next = "NEXT"  
pause = "PAUSE"  
print(f"{title:^105}",sep="")
print()
print('🔥▶️    Radio Gaga')
print(f'       {colorize("Queen", "yellow")}')
print()
print('PREV')
print(f'{colorize(next, "green"):>19}') #utilizando alignment e variáveis
print(f'{colorize("PAUSE", "purple"):>26}') #jeitinho que meu amor me ensinou

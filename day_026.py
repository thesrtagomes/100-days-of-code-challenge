# import os
# import time

# import pygame

# pygame.init()
# pygame.mixer.init()
# sound = pygame.mixer.Sound('audio.wav')
# sound.play()
# pygame.mixer.pause()

# def pause():
#   pygame.mixer.pause()

# pause()

# def play():
#   # Play the sound
#   pygame.mixer.unpause()
#   while True:
#     stop_playback = int(input('Press 2 anytime to pause playback and go back to the menu: '))
#     if stop_playback == 2:
#         pause()
#         return
#     else:
#       continue

# while True:
#     os.system("clear")
#     print('🎵 MyPOD Music Player')
#     time.sleep(2)
#     print ('Press 1 to Play')
#     print('Press 2 to Exit')
#     print("Press anything else to see the menu again")
#     user_press= int(input())

#     if user_press == 1:
#       print("Playing some proper tunes!")
#       play()
#     elif user_press == 2:
#       exit()
#     else:
#      continue

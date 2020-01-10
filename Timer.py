'''
import time
import pygame
import threading
def start_sound():

    pygame.mixer.init()
    pygame.mixer.music.load("z.ogg")
    pygame.mixer.music.play()

d = threading.Thread(target=start_sound)
d.setDaemon(True)
d.start()

'''

a = 5
for i in range(1,10000):
    a += 5
    print(a)
    if a>6000:
        print('hello')

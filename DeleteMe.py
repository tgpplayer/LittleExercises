import pyautogui as pg
import time

time.sleep(2)
# txt = open("animal.txt", "r")

# for i in txt:
#     pg.write("Usted es " + i)
#     pg.press('Enter')

for i in range(20):
    pg.write("Juegas?")
    time.sleep(0.5)
    pg.press("Enter")

# pg.write("AY MI GFA")
# pg.press('Enter')
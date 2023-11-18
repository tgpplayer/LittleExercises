import pyautogui as pg
import time

time.sleep(2)
txt = open("animal.txt", "r")

for i in txt:
pg.write("Usted es " + i)
pg.press('Enter')

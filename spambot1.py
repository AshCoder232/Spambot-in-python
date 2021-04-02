import pyautogui
import time

def Sendmsg():
  time.sleep(10);
  text=open("mrrobot.txt")
  for line1 in text:
    pyautogui.typewrite(line1)
    pyautogui.press('enter')
    time.sleep(0.8)

Sendmsg()


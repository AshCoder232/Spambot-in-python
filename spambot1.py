import pyautogui
import time

def Sendmsg():
  time.sleep(10);
  filename=input('enter file name:')
  fh=open("filename.txt")
  for line1 in fh:
    pyautogui.typewrite(line1)
    pyautogui.press('enter')
    time.sleep(0.1)

Sendmsg()


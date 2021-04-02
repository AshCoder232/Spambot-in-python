import pyautogui
import time


def Sendmsg():
   
    filename = input('enter file name:')
    fh = open(filename)
    time.sleep(10)
    for line1 in fh:        
        pyautogui.typewrite(line1)
        pyautogui.press('enter')
        


Sendmsg()

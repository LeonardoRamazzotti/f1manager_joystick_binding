import mouse 
import keyboard 
import pyautogui


def mouse():
    
    print(pyautogui.position())
        
    return
    
while True:
    
    if keyboard.is_pressed("ctrl+a"):
        mouse()    
        
        break
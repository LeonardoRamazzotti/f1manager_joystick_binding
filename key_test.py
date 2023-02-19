import mouse 
import keyboard 
import time

def test():
    mouse.move(261,677)
    time.sleep(0.2)
    mouse.click('left')
    time.sleep(0.2)
    mouse.move(58,565)
    time.sleep(0.2)
    mouse.click('left')
    time.sleep(0.2)
    mouse.move(261,677)
    time.sleep(0.2)
    mouse.click('left')



while True:
    
    if keyboard.is_pressed("ctrl+a"):
        test()    
        
        break
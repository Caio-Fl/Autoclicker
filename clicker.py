import time
import threading
import pyautogui
from random import randrange
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
#pip install pynput
#pip install pyautogui

print("\nWelcome to Autoclicker Bot!")
print("\nTo activate the Autoclicker press - key")
print("To increase the time between clicks press w key")
print("To reduce the time between clicks press s key")
print("To activate multi point click press q key\n")

TOGGLE_KEY = KeyCode(char="-")
TOGGLE_KEY_UP = KeyCode(char="w") 
TOGGLE_KEY_DOWN = KeyCode(char="s")
TOGGLE_KEY_MULTI = KeyCode(char="q")
clicking = False
multi = False
mouse = Controller()
tf = 0.2
ti = 0.2

def clicker():
    while True:
        ti = tf
        if clicking:
            mouse.click(Button.left, 1)
            if multi: # Se o modo multi estiver ativado aplica clicks em pontos aleatórios dentro de uma certa região onde o autoclick foi ativado apertando "="
                pyautogui.moveTo(currentMouseX+(40+randrange(10)), currentMouseY+(randrange(50)))
                time.sleep(0.2+0.01*randrange(1)) 
                mouse.click(Button.left, 1)
                pyautogui.moveTo(currentMouseX-(40+randrange(10)), currentMouseY+(randrange(50)))
                time.sleep(0.2+0.01*randrange(1))  
                mouse.click(Button.left, 1)
                pyautogui.moveTo(currentMouseX+(80+randrange(10)), currentMouseY+(randrange(50)))         
                mouse.click(Button.left, 1)
                time.sleep(0.2+0.01*randrange(1)) 
                pyautogui.moveTo(currentMouseX-(80+randrange(10)), currentMouseY+(randrange(50))) 

            time.sleep(ti+0.002*randrange(1)) 
            count = count + 1
            if count == 30:
                count = 0
                time.sleep(1)
        
def toggle_event(key):
    if key == TOGGLE_KEY: # Ativa o autoclick ao apertar TOGGLE_KEY "="
        global clicking
        clicking = not clicking
        global currentMouseX,currentMouseY
        currentMouseX, currentMouseY = pyautogui.position()
        if clicking:
            print("\nAutoclicker: ON")
        else:
            print("\nAutoclicker: OFF")
        
    if key == TOGGLE_KEY_UP: #Aumenta o tempo entre clicks
        global tf
        global ti
        tf = ti + 0.001
        ti = tf
        print("\nTime between clicks increased: ",round(tf*1000,1), "ms")
    if key == TOGGLE_KEY_DOWN: #Diminui o tempo entre clicks
        tf = ti - 0.001
        if tf < 0.0001:
            tf = 0.0001
        ti = tf
        print("\nTime between clicks reduced: ",round(tf*1000,1), "ms")
    if key == TOGGLE_KEY_MULTI: # Ativa o modo multi ao clicar em TOGGLE_KEY_MULTI " ' "
        global multi
        multi = not multi
        if multi:
            print("\nMulti Tap: ON")
        else:
            print("\nMulti Tap: OFF")

click_thread = threading.Thread(target=clicker)
click_thread.start()


with Listener(on_press=toggle_event) as listener:
    
    listener.join()

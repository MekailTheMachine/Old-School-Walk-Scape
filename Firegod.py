import time
import threading
import pyautogui
import mouse
import random as rnd
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

global running
global seshs
global burnt

ONOFF = KeyCode(char="1")
KEY = KeyCode(char ='2')

seshs = int (0)
burnt = int (0)
xpus = int (0)
ypus = int(0)
running = False


def winemaker():
    while True:
        if running:
            print ("Let's burn up yo!")
            global seshs
            global burnt

            ## ~~~ Random mouse movement ~~~~ ####

            pyautogui.moveTo(rnd.randint(700,980), rnd.randint(100,480), 0.33 + 0.5 * rnd.random() + 3/27 * rnd.random())
            pyautogui.moveRel(rnd.randint(-40, 74), rnd.randint(-21,20), 0.33 + 0.5 * rnd.random() + 3/27 * rnd.random())
            time.sleep(0.13 + 0.5 * rnd.random() + 3/27 * rnd.random())
            pyautogui.moveRel(rnd.randint(-40, 74), rnd.randint(2,60), 0.33 + rnd.random() + 3/27 * rnd.random() * 1.2 + 1) # random movement
            time.sleep(0.13 + 0.5 * rnd.random() + 3/27 * rnd.random())
            ## ~~~ Random mouse movement ~~~~ ####

            # Begin opening bank: 
            if (seshs == 0):
                pyautogui.moveTo(rnd.randint(113,136), rnd.randint(538,556), 0.83 + 0.5 * rnd.random() + 3/27 * rnd.random()) # move mouse to left side of bank for first round.
                time.sleep(rnd.random() * 0.2 + 0.3) # wait before next action, use .1 multiplier because we aren't moving mouse position. 
                mouse.click()
                time.sleep(8.8 + 1.23 * rnd.random()) # sleep. 
            
            if (seshs > 0 and seshs % 2 == 0): 
                pyautogui.moveTo(rnd.randint(900,910), rnd.randint(517,534), 0.83 + 0.5 * rnd.random() + 3/27 * rnd.random())
                time.sleep(rnd.random() * 0.2 + 0.3) # wait before next action, use .1 multiplier because we aren't moving mouse position. 
                mouse.right_click() # Open up banker options with right click.
                time.sleep(rnd.random() * 0.1 + 0.15) # Sleep 
                pyautogui.moveRel(rnd.randint(0, 5), rnd.randint(38,40), 0.2 + 0.3 * rnd.random()) #Move mouse down to open bank
                print("Openede bank at:", pyautogui.position()) # print position           
                time.sleep((rnd.random() * 0.2 + 0.02)) # Short sleep 
                mouse.click() #open up the bank.
                time.sleep(1 + 1.23 * rnd.random()) # sleep.
            elif (seshs > 0 and (seshs + 1) % 2 == 0): 
                pyautogui.moveTo(rnd.randint(866,872), rnd.randint(558,566), 0.83 + 0.5 * rnd.random() + 3/27 * rnd.random())
                time.sleep(rnd.random() * 0.2 + 0.3) # wait before next action, use .1 multiplier because we aren't moving mouse position. 
                mouse.right_click() # Open up banker options with right click.
                time.sleep(rnd.random() * 0.1 + 0.15) # Sleep 
                pyautogui.moveRel(rnd.randint(0, 5), rnd.randint(38,40), 0.2 + 0.3 * rnd.random()) #Move mouse down to open bank
                print("Openede bank at:", pyautogui.position()) # print position           
                time.sleep((rnd.random() * 0.2 + 0.02)) # Short sleep 
                mouse.click() #open up the bank.
                time.sleep(0.02 + 1.23 * rnd.random()) # sleep.
            


            print ("Getting wood.")
            pyautogui.moveTo(rnd.randint(986, 1004), rnd.randint(166, 172), rnd.random() * 0.133 + 0.36) # move to wood
            time.sleep(rnd.random()* 0.0173 + 0.41) #Sleep
            mouse.right_click() #open wood options now.
            time.sleep(0.18 * rnd.random() +0.2) #sleep
            pyautogui.moveRel(rnd.randint(-12, 5), rnd.randint(100, 107), rnd.random() * 0.12 + 0.12) #move mouse down to quantity of ALL
            time.sleep(rnd.random() * 0.19 + 0.29)
            mouse.click() #Get wood
            print (" Let's get ready to burn!!")
            #

            # BURN PROCESS BEGIN !

            ## ~~~ Random mouse movement ~~~~ ####
            pyautogui.moveRel(rnd.randint(-20,40), rnd.randint(-10,6), rnd.random() * 0.12 + 0.03) #Move around from current spot
            time.sleep(rnd.random() * 0.03 + 0.006) #Sleep
            ## ~~~ Random mouse movement ~~~~ ####

            #Exit out of bank (first term)
            if ( seshs % 2 == 0 ):
                pyautogui.moveTo(rnd.randint(1669, 1672), rnd.randint(513, 520), rnd.random() * 0.13 + 0.84) # X of the bank (headed to opposite post)
            elif ( (seshs +1) % 2 == 0):
                pyautogui.moveTo(rnd.randint(1669, 1672), rnd.randint(555, 565), rnd.random() * 0.13 + 0.84)
            time.sleep(0.321 + rnd.random() *0.098)
            mouse.click()
            time.sleep(0.321 + rnd.random() *0.098)
            pyautogui.moveRel(rnd.randint(-8, 12), rnd.randint(70,140), rnd.random() * 0.3 + 0.031) # random movement
            time.sleep(rnd.random() * 0.987 + 10.8) #sleep
            
            ## ~~~ Random mouse movement ~~~~ ####
            pyautogui.moveRel(rnd.randint(-20,40), rnd.randint(100,200), rnd.random() * 0.13 + 0.15) #Move around from current spot
            pyautogui.moveRel(rnd.randint(-2, 12), rnd.randint(6,12), rnd.random() * 0.13 + 0.15) # random movement
            time.sleep(rnd.random() * 0.13 + 0.01) #Sleep
            ## ~~~ Random mouse movement ~~~~ ####



            # Time to burn logs, this portion is extensive...
            xpus = 1755
            ypus = 765
            for i in range (1, 28):
                pyautogui.moveTo(rnd.randint(1709,1720), rnd.randint(752, 768), rnd.random() * 0.13 + 0.197) #move to tinder box
                time.sleep(rnd.random() *0.01 + 0.29)
                mouse.click() #use tinder box
                time.sleep(rnd.random() *0.01 + 0.298)
                pyautogui.moveTo(rnd.randint(xpus - 3, xpus + 3), rnd.randint(ypus - 3, ypus + 3), rnd.random() * 0.13 + 0.237) # move to log 
                time.sleep(rnd.random() * 0.01 + 0.30)
                mouse.click() # burn log 1 
                burnt = burnt + 1
                print ("burnt amount is", burnt)
                if (burnt == 1):
                    time.sleep(rnd.random() *0.13 + 0.93) # Sleep for an extra 0.9 seconds on the first burn
                xpus = xpus + 40
                if ((burnt + 1) % 4 == 0 or burnt == 3):
                    ypus = ypus + 35 # drop the mouse down one row of items for the next iteration
                    xpus = xpus - 160 # pull mouse back to the first coulum for the next iteration
                    time.sleep( 0.88 + rnd.random() *0.05)
                if ((burnt + 2) % 4 == 0 or burnt == 3):
                    time.sleep( 0.33 + rnd.random() *0.01)


            print (" All done!")
            seshs = seshs + 1
            print ("This is batch number:", seshs)
            pyautogui.moveTo(rnd.randint(856,864), rnd.randint(560,586), 0.83 + 0.5 * rnd.random() + 3/27 * rnd.random()) # move mouse to banker.
            burnt = 0

            #End of wine run; time to sleep and repeat     
        time.sleep(rnd.random() * rnd.random() + 0.9)


def togglebot(key):
    if key == ONOFF:
        global running
        print ("Program is on:", not running)
        running = not running
    elif key == KEY: 
        print ("Kill switch acitaved")
        running = False
        exit() # This will end the program entirely
        sys.exit()

click_thread = threading.Thread(target=winemaker)
click_thread.start()

with Listener(on_press=togglebot) as listner:
    listner.join()
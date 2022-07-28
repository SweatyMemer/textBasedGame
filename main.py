import colorama as col
import imageToAscii
from time import sleep
from random import randint
from os import system
from time import time
col.init(autoreset=True)

class imageClass:
    xavier = 0
    dudong = 1



def pogLog(*aa):
    with open("log.txt", 'a') as f:
        f.writelines(str(aa))

def getStoredAscii() -> str:
    with open("output.txt") as f:
        storedAscii = f.read().split("|")   
        return storedAscii 


def displayImage(asciiImage, colour = col.Fore.WHITE) -> bool:
    try:
        imageToAscii.changeFontSize(2,2)
        if len(asciiImage) > 100:
            lines = asciiImage.split("\n")
            width = len(lines[1])
            height = len(lines)
            imageToAscii.terminalSize(width,height)
            # pogLog(width,height)
            print(colour + asciiImage)
            return True
    except:
        return False


def displayImageRange(asciiImageList, start, stop, step=1, colour = col.Fore.WHITE) -> bool:
    i=start
    while i<stop:
        displayImage(colour + getStoredAscii()[i])
        i += step

class school:
    
    def __init__(self):
        subject = randint(0,2)
        if subject == 0:
            print("You choose to study maths")
            self.maths()
        elif subject == 1:
            print("You choose to study maths")
            self.maths()
        elif subject == 2:
            print("You choose to study maths")
            self.maths()
            
    def maths(self):
        num1 = randint(0,20)
        num2 = randint(0,20)
        operator = randint(0,1)
        if operator == 0:
            answer = num1 + num2
            startTime = int(time())
            userInput = input(f"{num1} + {num2} = ")
            if userInput == str(answer) and int(time()) - startTime < 5:
                print(f"Correct! {num1} + {num2} = {answer}")
                return True
            elif userInput != answer:
                print(f"Your answer is wrong, the correct answer is {answer}")
                return False
            elif userInput == answer and int(time()) - startTime > 5:
                print(f"Your answer is correct, but you took too long to answer, you have 5 seconds to answer.")
                return False
        elif operator == 1:
            answer = num1 - num2
            startTime = int(time())
            userInput = input(f"{num1} - {num2} = ")
            if userInput == str(answer) and int(time()) - startTime < 5:
                print(f"Correct! {num1} - {num2} = {answer}")
                return True
            elif userInput != answer:
                print(f"Your answer is wrong, the correct answer is {answer}")
                return False
            elif userInput == answer and int(time()) - startTime > 5:
                print(f"Your answer is correct, but you took too long to answer, you have 5 seconds to answer.")
                return False

class Character:
    def __init__(self, maxPP: int, PP: int, maxHP: int, HP: int, inventory: dict):
        self.maxPP = maxPP
        self.PP = PP
        self.maxHP = maxHP
        self.HP = HP
        self.inventory = inventory
    
    

class day:
    def __init__(self, apparition: bool, eliteApparition: bool = False):
        self.apparition = apparition
        self.eliteApparition = eliteApparition
        self.totalDays = 0
    
    def stepDay(self):
        if randint(1,10) == 1:
            self.apparition = True
        else:
            self.apparition = False

def wait(time: int):
    for i in range(time):
        sleep(1)
        print(".", end="")
    print("")

def main():
    displayImage(getStoredAscii()[imageClass.dudong])
    sleep(3)
    imageToAscii.terminalDefault()
    
    MC = Character(100,100,100,100,{})
    print("You have recently moved to a new school for study, and you have a free period and decide to go straight to your dorm.\nYou walk into your dorm and see a student who introduces himself to you as your roommate, Xavier")
    input(f"{col.Fore.YELLOW}Press any key to continue")
    system('cls')
    print("You begin your school day")
    wait(2)
    if school():
        MC.maxPP += 10
        MC.PP += 10
        print("You have gained 10 PP")
    input(vars(MC))

if __name__ == "__main__":
    main()
    imageToAscii.terminalDefault()

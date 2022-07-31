from typing import List
import colorama as col
import imageToAscii
from time import sleep
from random import randint
from os import system
from time import time
from itertools import zip_longest

col.init(autoreset=True)


class ImageClass:
    xavier = 0
    dudong = 1
    night = 2
    monster = 3


def pogLog(*aa):
    with open("log.txt", 'a') as f:
        f.writelines(str(aa))


def getStoredAscii() -> List[str]:
    with open("output.txt") as f:
        storedAscii = f.read().split("|")
        return storedAscii


def displayImage(asciiImage, colour=col.Fore.WHITE) -> bool:
    try:
        imageToAscii.changeFontSize(2, 2)
        if len(asciiImage) > 100:
            lines = asciiImage.split("\n")
            width = len(lines[1])
            height = len(lines)
            imageToAscii.terminalSize(width, height)
            # pogLog(width,height)
            print(colour + asciiImage)
            return True
    except:
        return False


def displayImageRange(asciiImageList, start, stop, step=1, colour=col.Fore.WHITE) -> bool:
    i = start
    while i < stop:
        displayImage(colour + asciiImageList[i])
        i += step
    return True


class school:
    def __init__(self):
        subject = randint(0, 2)
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
        num1 = randint(0, 20)
        num2 = randint(0, 20)
        operator = randint(0, 1)
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


class Weapon:
    def __init__(self, damage: int, PP: int, name: str = "Generic Sword"):
        self.damage = damage
        self.PP = PP
        self.name = name


class Character:
    def __init__(self, maxPP: int, PP: int, maxHP: int, HP: int, defence: int, inventory: dict, friendly: bool,
                 MC: bool, equippedWeapon: Weapon, alive: bool, name: str):
        self.maxPP = maxPP
        self.PP = PP
        self.maxHP = maxHP
        self.HP = HP
        self.defence = defence
        self.inventory = inventory
        self.MC = MC
        self.friendly = friendly
        self.equippedWeapon = equippedWeapon
        self.alive = alive
        self.name = name

    def takeDamage(self, damage: int):
        if randint(0, int(self.defence / 10)) == 0:
            self.HP -= damage
            print(f"{self.name} took {damage} damage")
            if int(self.HP) <= 0:
                self.alive = False
                print(f"{self.name} died")
        else:
            self.HP -= (damage / 2)
            print(f"{self.name} took {damage / 2} damage")

    def takeTruedamage(self, damage: int):
        self.HP -= damage
        print(f"{self.name} took {damage} damage")
        if self.HP <= 0:
            self.alive = False
            print(f"{self.name} died")

    def heal(self, heal: int):
        self.HP += heal
        print(f"{self.name} healed {heal} HP")


class day:
    def __init__(self, apparition: bool, eliteApparition: bool = False):
        self.apparition = apparition
        self.eliteApparition = eliteApparition
        self.totalDays = 0

    def stepDay(self):
        if randint(1, 10) == 1:
            self.apparition = True
        else:
            self.apparition = False


def wait(duration: int):
    for i in range(duration):
        sleep(1)
        print(".", end="")
    print("")


def print_lines(*lines: str):
    """
    A helpful function for printing many
    separate strings on separate lines.
    """
    print("\n".join([line for line in lines]))


class battle:
    def __init__(self, *characters: Character) -> None:
        pass

    def start(self, *characters: Character):

        self.friendlyCharacters = []
        self.hostileCharacters = []

        for character in characters:
            if character.friendly:
                self.friendlyCharacters.append(character)
            else:
                self.hostileCharacters.append(character)

        whoGoesFirst = randint(0, 1)
        wait(2)
        while 1:
            self.printBattle(self.friendlyCharacters, self.hostileCharacters)
            for fC in self.friendlyCharacters:
                if whoGoesFirst == 0:  # if the coinflip returns 0 then it skips the friendlies turn for the first round, making the hostiles go first
                    whoGoesFirst = 1
                    break
                if fC.MC:  # if the friendly character is the main character give them some choices on the attack
                    wait(1)
                    print_lines(
                        f"1 - Basic Attack: {fC.equippedWeapon.damage} (chance of doing half damage with opponents defence)",
                        f"2 - Psychic Attack: {fC.equippedWeapon.PP}",
                        f"3 - Analyse - Grants increased critical chance for the next turn",
                        f"HP: {fC.HP} | PP: {fC.PP}"
                    )
                    IN = input("> ")
                    if IN == "1":
                        for hC in self.hostileCharacters:
                            if hC.alive and fC.alive:
                                wait(1)
                                hC.takeDamage(fC.equippedWeapon.damage)
                                break
                            else:
                                pass
                    elif IN == "2":
                        for hC in self.hostileCharacters:
                            if fC.PP > fC.equippedWeapon.PP / 2:
                                if hC.alive and fC.alive:
                                    wait(1)
                                    hC.takeTruedamage(fC.equippedWeapon.PP)
                                    fC.PP -= fC.equippedWeapon.PP / 2
                                    break
                                else:
                                    pass
                            else:
                                print(
                                    f"You don't have enough PP to use this attack, {fC.PP} when you need {fC.equippedWeapon.PP / 2}")
                    elif IN == "3":
                        print("Increased critical chance for next turn. RN this is complete cap tho")

                else:  # if the character isn't a main character we just do the damage that their weapon does
                    for hC in self.hostileCharacters:
                        if hC.alive and fC.alive:
                            wait(1)
                            hC.takeDamage(fC.equippedWeapon.damage)
                            break
                        else:
                            pass
            for hC in self.hostileCharacters:
                for fC in self.friendlyCharacters:
                    if fC.alive and hC.alive:
                        wait(1)
                        fC.takeDamage(hC.equippedWeapon.damage)
                        break
                    else:
                        pass
            result = all(not obj.alive for obj in self.friendlyCharacters)
            if result:
                print("Your party has been defeated!")
                return False  # if all friendlies are dead return False, a failure
            else:
                pass
            # print("!!!" + hC.alive for hC in self.hostileCharacters)
            result = all(not hC.alive for hC in self.hostileCharacters)
            if result:
                print("You have defeated all the enemies!")
                return True  # if all enemies are dead return True, a victory
            else:
                pass

    def printBattle(self, friendlyCharacters: List[Character], hostileCharacters: List[Character]):
        for friendlychar, hostilechar in zip_longest(friendlyCharacters, hostileCharacters):
            print(f"""{friendlychar.name} : {friendlychar.HP} {' ' * 20} {hostilechar.name} : {hostilechar.HP}""")


def printInventory(inventory: dict):
    for item in inventory:
        if item.type == Weapon:
            print(f"{col.Fore.BLUE}{item[0]} : {item[1]}")
        else:
            print(item)


def main():
    imageArray = getStoredAscii()

    displayImage(imageArray[ImageClass.dudong])
    sleep(3)
    imageToAscii.terminalDefault()

    currentDay = day(True, False)

    MainCharacter = Character(100, 100, 100, 100, 10, {Weapon(20, 20, "Cursed Sword"): 1}, True, True, Weapon(20, 20),
                              True, input("What is your name? "))
    print(
        "You have recently moved to a new school for study, and you have a free period and decide to go straight to "
        "your dorm.\nYou walk into your dorm and see a student who introduces himself to you as your roommate, Xavier")
    input(f"{col.Fore.YELLOW}Press any key to continue")
    system('cls')
    print("You begin your school day")
    wait(2)
    if school():
        MainCharacter.maxPP += 10
        MainCharacter.PP += 10
        print("You have gained 10 PP")

    if currentDay.apparition:
        print("You hear rumours around the school about a missing student, nobody knows where they are")
        wait(3)
        system('cls')
    print("You decide to retire early as it's your first day and you are tired.")
    wait(2)
    displayImage(imageArray[ImageClass.night])
    sleep(8)
    imageToAscii.terminalDefault()

    if currentDay.apparition:
        print_lines(
            "You are awoken by a demonic looking apparition, sitting at the foot of your bed",
            "Your roommate Xavier is standing staring at the monster, a knife in hand."
        )
        wait(3)
        displayImage(imageArray[ImageClass.monster])
        sleep(0.4)
        imageToAscii.terminalDefault()
        print("Battle Starting", end="")
        enemy = Character(100, 100, 100, 100, 10, {}, False, False, Weapon(10, 10), True, "Thicc enemy dumptruck")
        enemy2 = Character(100, 100, 100, 100, 10, {}, False, False, Weapon(10, 10), True, "not as thicc enemy")
        friend1 = Character(100, 100, 100, 100, 100, {}, True, False, Weapon(20, 20), True, "Xavier")
        wait(2)
        battle().start(MainCharacter, friend1, enemy, enemy2)

    input(vars(MainCharacter))


if __name__ == "__main__":
    main()
    imageToAscii.terminalDefault()

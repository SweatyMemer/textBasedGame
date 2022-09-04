from typing import List
import colorama as col
import imageToAscii
from time import sleep
from random import randint, choice
from os import system
from time import time
from itertools import zip_longest
from winsound import Beep
from csv import reader
import keyboard

col.init(autoreset=True)


class ImageClass:
    xavier = 0
    dudong = 1
    night = 2
    monster = 3
    backroomStart = 4


musicNotes = {"C": 262, "D": 294, "E": 330, "F": 349, "G": 392, "A": 440, "B": 494}


class position:
    def __init__(self, xValue, yValue, facingValue):
        self.x = xValue
        self.y = yValue
        self.facing = facingValue


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


imageArray = getStoredAscii()
backroomStart = ImageClass.backroomStart

mirrorWorldMap = [[[imageArray[backroomStart], imageArray[backroomStart + 1], imageArray[backroomStart + 2],
                    imageArray[backroomStart + 3]],
                   [imageArray[backroomStart + 4], imageArray[backroomStart + 5], imageArray[backroomStart + 6],
                    imageArray[backroomStart + 7]],
                   [imageArray[backroomStart + 8], imageArray[backroomStart + 9], imageArray[backroomStart + 10],
                    imageArray[backroomStart + 11]]],
                  [[imageArray[backroomStart + 12], imageArray[backroomStart + 13], imageArray[backroomStart + 14],
                    imageArray[backroomStart + 15]],
                   [imageArray[backroomStart + 16], imageArray[backroomStart + 17], imageArray[backroomStart + 18],
                    imageArray[backroomStart + 19]],
                   [imageArray[backroomStart + 20], imageArray[backroomStart + 21], imageArray[backroomStart + 22],
                    imageArray[backroomStart + 23]]],
                  [[imageArray[backroomStart + 24], imageArray[backroomStart + 25], imageArray[backroomStart + 26],
                    imageArray[backroomStart + 27]],
                   [imageArray[backroomStart + 28], imageArray[backroomStart + 29], imageArray[backroomStart + 30],
                    imageArray[backroomStart + 31]],
                   [imageArray[backroomStart + 32], imageArray[backroomStart + 33], imageArray[backroomStart + 34],
                    imageArray[backroomStart + 35]]],
                  [[imageArray[backroomStart + 36], imageArray[backroomStart + 37], imageArray[backroomStart + 38],
                    imageArray[backroomStart + 39]],
                   [imageArray[backroomStart + 40], imageArray[backroomStart + 41], imageArray[backroomStart + 42],
                    imageArray[backroomStart + 43]],
                   [imageArray[backroomStart + 44], imageArray[backroomStart + 45], imageArray[backroomStart + 46],
                    imageArray[backroomStart + 47]]]]


class HealthPot:
    def __init__(self, healing: float, name: str):
        self.healing = healing
        self.name = name

    def __repr__(self):
        return f"Name, {self.name}, Healing {self.healing}"


class Weapon:
    def __init__(self, damage: float, PP: float, name: str = "Generic Sword"):
        self.damage = damage
        self.PP = PP
        self.name = name

    def __repr__(self):
        return f"Name: {self.name}, Psychic Power: {self.PP}, Damage: {self.damage}"


class bossSummon:
    def __init__(self):
        self.count = 1
        self.name = "Strange crystal"

    def add(self, countToAdd):
        self.count += countToAdd

    def subtract(self, countToSubtract):
        self.count -= countToSubtract


class Character:
    def __init__(self, maxPP: int, PP: int, maxHP: int, HP: int, defence: int, inventory: list, friendly: bool,
                 MC: bool, equippedWeapon: Weapon, alive: bool, name: str, money: int = 0):
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
        self.money = money

    def takeDamage(self, damage: float):
        if randint(0, int(self.defence / 10)) == 0:
            self.HP -= damage
            print(f"{self.name} took {damage} damage")
            if int(self.HP) <= 0:
                self.alive = False
                print(f"{self.name} died")
        else:
            self.HP -= (damage / 2)
            print(f"{self.name} took {damage / 2} damage")
            if int(self.HP) <= 0:
                self.alive = False
                print(f"{self.name} died")

    def takeTruedamage(self, damage: float):
        self.HP -= damage
        print(f"{self.name} took {damage} damage")
        if self.HP <= 0:
            self.alive = False
            print(f"{self.name} died")

    def heal(self, heal: int):
        startingHealth = self.HP

        if self.HP + heal > self.maxHP:
            self.HP = self.maxHP
        else:
            self.HP += heal

        endingHealth = self.HP
        print(f"{self.name} healed {endingHealth - startingHealth} HP")

    def showInventory(self):
        num = 0
        for item in self.inventory:
            print(f"{num} :: {item.name}")
            num += 1
        print(f"Money: {self.money}")

    # idea for the inventory system
    # make it a list
    # print it in a for loop with the number of the list next to the item name
    #
    # num = 0
    # for i in inventory: (the inventory is a list)
    #     print({num} - {i})
    #     num += 1

    def selectItem(self):
        self.showInventory()
        print(
            "select an item to use, choosing a weapon will swap it out for your current one, choosing any other item will use it accordingly")
        item = input("item: ")
        try:
            item = int(item)
        except:
            print("DUDE LITERALLY TYPE A NUMBER IDOT")
            self.selectItem()
        if isinstance(self.inventory[item], Weapon):
            self.inventory.append(self.equippedWeapon)  # put equipped weapon into inventory
            self.equippedWeapon = self.inventory[item]
            del self.inventory[item]
            print(f"Current weapon {self.equippedWeapon}")
        elif isinstance(self.inventory[item], HealthPot):
            self.heal(self.inventory[item].healing)
            del self.inventory[item]
        elif isinstance(self.inventory[item], HealthPot) and self.inventory[
            item].name == f"{col.Fore.RED}HEALTH POT OF ORTH":
            self.heal(self.inventory[item].healing)

        # if isinstance(self.inventory[item], Weapon):
        #     self.inventory[self.equippedWeapon.name] = self.equippedWeapon #  put equipped weapon into inventory
        #     self.equippedWeapon = self.inventory[item] #  set the equipped weapon to the item
        #     del self.inventory[item] #  delete the item from the list so that they don't have 2 of them
        #     print(f"Current equipped weapon: {self.equippedWeapon}")
        # elif isinstance(self.inventory[item], HealthPot):
        #     self.heal(self.inventory[item].healing)
        # else:
        #     print(f"You can't use {item}, idot")


class school():

    def __init__(self, char: Character):
        subject = randint(0, 2)

        if subject == 0:
            print("You choose to study maths")
            self.maths(char)
            return
        elif subject == 1:
            print("You choose to study maths")
            self.music(char)
            return
        elif subject == 2:
            print("You choose to study maths")
            self.maths(char)
            return

    def maths(self, char: Character):
        num1 = randint(0, 20)
        num2 = randint(0, 20)
        operator = randint(0, 1)
        if operator == 0:
            answer = num1 + num2
            startTime = int(time())
            userInput = input(f"{num1} + {num2} = ")
            if userInput == str(answer) and int(time()) - startTime < 5:
                print(f"Correct! {num1} + {num2} = {answer}")
                char.maxPP += 10
                char.PP += 10
                print(f"new maxPP is {char.maxPP}")
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
                char.maxPP += 10
                char.PP += 10
                print(f"new max PP is {char.maxPP}")
                return True
            elif userInput != answer:
                print(f"Your answer is wrong, the correct answer is {answer}")
                return False
            elif userInput == answer and int(time()) - startTime > 5:
                print(f"Your answer is correct, but you took too long to answer, you have 5 seconds to answer.")
                return False

    def music(self, char: Character):
        print("You choose to study music! ")
        print("This note is C")
        Beep(musicNotes["C"], 3000)
        wait(2)
        print("What note is this?")
        noteName, note = choice(list(musicNotes.items()))

        def listen():
            Beep(note, 3000)
            INPUT = input("What note was that? (A, B, C, D, E, F, G), type 'again' to hear again\n> ")
            if INPUT.lower() == noteName.lower():
                print("Good job, you earned 10 health and 10 PP")
                char.maxPP += 10
                char.PP += 10

                char.maxHP += 10
                char.HP += 10
            elif INPUT == "again":
                listen()
                return
            else:
                print("Wrong,", end="")

        listen()
        print("the note was", noteName, ":", note, "hz")


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
    """
    A function for waiting a specified amount of time and prints fullstops (to please the user)
    """
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

def die():
    imageToAscii.imageToAscii("youdied.jpg")
    input("You died, press enter to exit")
    exit()


class battle:
    def __init__(self, *characters: Character) -> None:
        pass

    def start(self, mainChar: Character, *characters: Character) -> bool:

        self.friendlyCharacters = []
        self.hostileCharacters = []
        MainCharacter = mainChar

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
                if fC.MC and fC.alive:  # if the friendly character is the main character give them some choices on the attack
                    wait(1)
                    print_lines(
                        f"1 - Basic Attack: {fC.equippedWeapon.damage} (chance of doing half damage with opponents defence)",
                        f"2 - Psychic Attack: {fC.equippedWeapon.PP}",
                        f"3 - Analyse - Grants increased critical chance for the next turn",
                        f"4 - Use an item from your inventory",
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
                    elif IN == "4":
                        fC.selectItem()

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
            if result:  # dropping items and stuff in here
                print("You have defeated all the enemies!")
                earnedItems = []
                for hC in self.hostileCharacters:
                    combinedItems = hC.inventory + [hC.equippedWeapon]
                    for item in combinedItems:
                        if randint(0, 1) == 1:
                            earnedItems.append(item)
                    randomResult = randint(0, 5)
                    if randomResult == 5 and not any(isinstance(x, bossSummon) for x in mainChar.inventory):
                        mainChar.inventory.append(bossSummon())
                    elif randomResult == 5 and any(isinstance(x, bossSummon) for x in mainChar.inventory):
                        for (index, x) in enumerate(mainChar.inventory):
                            if x.name == "Strange crystal":
                                summonsIndex = index
                        mainChar.inventory[summonsIndex].add(1)
                        print(
                            f"You now have {mainChar.inventory[summonsIndex].count} boss summons, you need 3 to summon a boss")
                print(f"You gained new items!")
                for i in earnedItems:
                    print(i)
                MainCharacter.inventory.extend(earnedItems)
                return True  # if all enemies are dead return True, a victory
            else:
                pass

    def printBattle(self, friendlyCharacters: List[Character], hostileCharacters: List[Character]):
        for friendlychar, hostilechar in zip_longest(friendlyCharacters, hostileCharacters):
            if friendlychar is None and hostilechar is not None:
                print(f"{' ' * 35} {hostilechar.name} : {hostilechar.HP}")
            elif friendlychar is not None and hostilechar is None:
                print(f"{friendlychar.name} : {friendlychar.HP}")
            elif friendlychar is not None and hostilechar is not None:
                print(f"{friendlychar.name} : {friendlychar.HP} {' ' * 20} {hostilechar.name} : {hostilechar.HP})")


def showShopInventory(inventory: list):
    num = 0
    for item in inventory:
        print(f"{num} :: {item[0].name}, ${item[1]}")
        num += 1


class weapons:
    swordOfOrth = Weapon(2000, 1000, f"{col.Fore.RED}SWORD OF ORTH{col.Fore.RESET}")
    genericSword = Weapon(20, 20, f"Generic Sword")
    longSword = Weapon(30, 30, "Long Sword")
    weakSword = Weapon(10, 10, "Weak Sword")


class healthPots:
    healthOfOrth = HealthPot(5000, f"{col.Fore.RED}HEALTH POT OF ORTH{col.Fore.RESET}")
    largeHealing = HealthPot(100, "Large Healing")
    mediumHealing = HealthPot(50, "Medium Healing")
    smallHealing = HealthPot(20, "Small Healing")


class town:
    def __init__(self, MainCharacter: Character):
        print_lines(
            "Do you want to go to:",
            "1: Shop",
            "2: Blacksmith"
        )

        self.shopInventory = [(weapons.longSword, 100), (weapons.swordOfOrth, 1000), (healthPots.smallHealing, 10),
                              (healthPots.mediumHealing, 20), (healthPots.largeHealing, 50)]

        INPUT = input("> ")
        if INPUT == "1":
            self.shop(MainCharacter)
        if INPUT == "2":
            self.blacksmith(MainCharacter)

    def getPrice(self, itemToSell):
        if isinstance(itemToSell, Weapon):
            price = itemToSell.damage + itemToSell.PP
            return price

        elif isinstance(itemToSell, HealthPot):
            price = itemToSell.healing / 2
            return price

    def shop(self, MainCharacter: Character):
        def startOfShop():
            print("Welcome to the shop, would you like to buy or sell items? ")
            INPUT = input("1 : Buy\n2: Sell\n3: exit\n> ")
            if INPUT == "1":

                print("Here are my wares")
                showShopInventory(self.shopInventory)
                print(f"You have ${MainCharacter.money}")
                selectedItem = input("> ")
                try:
                    selectedItem = int(selectedItem)
                except:
                    print("use a number number idot")
                    startOfShop()
                    return

                if input(
                        f"Are you sure you want to buy {self.shopInventory[selectedItem][0]} (y/n) \n> ").lower() == 'y':
                    if MainCharacter.money >= self.shopInventory[selectedItem][1]:
                        MainCharacter.inventory.append(self.shopInventory[selectedItem][0])
                        MainCharacter.money -= self.shopInventory[selectedItem][1]
                        print(f"You have purchased {self.shopInventory[selectedItem][0]}")
                        wait(2)
                        print("Your inventory is now: ")
                        MainCharacter.showInventory()
                        startOfShop()
                        return
                    else:
                        print(
                            f"Insufficient funds, you have {MainCharacter.money}, you need {self.shopInventory[selectedItem][1]}")
                        startOfShop()
                        return

            if INPUT == '2':
                print("What do you want to sell?")
                MainCharacter.showInventory()
                selectedItem = input("> ")
                try:
                    selectedItem = int(selectedItem)
                except:
                    print("use a number number idot")
                    startOfShop()
                    return

                if len(MainCharacter.inventory) >= selectedItem and selectedItem >= 0:
                    if input(
                            f"Are you sure you want to sell {MainCharacter.inventory[selectedItem]} for {self.getPrice(MainCharacter.inventory[selectedItem])}").lower() == 'y':
                        MainCharacter.money += self.getPrice(MainCharacter.inventory[selectedItem])
                        del MainCharacter.inventory[selectedItem]
                        print("Transaction complete you now have ${}".format(MainCharacter.money))
                        startOfShop()
                        return
                    else:
                        startOfShop()
                        return
                else:
                    print("You don't have that item idot")
                    startOfShop()
                    return
            if INPUT == '3':
                return

        startOfShop()

    def getPriceOfUpgrade(self, levels: int):
        cost = 0.05 * levels * levels + 10
        return round(cost)

    def blacksmith(self, MainCharacter: Character):
        def startOfBlacksmith():
            print("Welcome to the blacksmith, is there a weapon that you want me to improve? (type x to exit)")
            MainCharacter.showInventory()
            #  select an item
            selectedItem = input("> ")
            if selectedItem == "x":
                return
            try:
                selectedItem = int(selectedItem)
            except:
                print("use a number number idot")
                startOfBlacksmith()
                return
            if not isinstance(MainCharacter.inventory[selectedItem], Weapon):
                print("You can only upgrade weapons")
                startOfBlacksmith()
                return
            levels = input("How many levels do you want to add to that weapon? \n> ")
            try:
                levels = int(levels)
            except:
                print("use a number idot")
                startOfBlacksmith()
                return
            INPUT = input(
                f"Do you want to upgrade {MainCharacter.inventory[selectedItem]} for {self.getPriceOfUpgrade(levels)}? (y/n)\n> ")
            if MainCharacter.money <= self.getPriceOfUpgrade(levels):
                print("you don't have enough money for that")
                startOfBlacksmith()
                return
            if INPUT == "y":
                MainCharacter.inventory[selectedItem].damage += levels
                MainCharacter.inventory[selectedItem].PP += levels
                MainCharacter.money -= self.getPriceOfUpgrade(levels)
                print(f"You have upgraded {MainCharacter.inventory[selectedItem]}, it now does {MainCharacter.inventory[selectedItem].damage} damage")
                wait(2)
            else:
                startOfBlacksmith()
                return

        startOfBlacksmith()


def choiceMenu(MainCharacter: Character):
    INPUT = input("Where do you want to go?\n\
0 :: Town (Where there are shops and blacksmiths\n\
1 :: Home (Where you can sleep and enter the alternate world\n\
> ")
    if INPUT == "0":
        town(MainCharacter)
    elif INPUT == "1":
        home(MainCharacter)


def getLineFromCsv(file, line: int = 0):
    output = []
    with open(file) as csvfile:
        csvReader = reader(csvfile)
        for line in csvReader:
            output.append(line)
        return output[0]


def pickRandomHostiles(count: int, difficulty: int):
    hostiles = []
    hostileNames = getLineFromCsv("hostileNames.csv")
    for i in range(count):
        hostileInventory = []

        for item in range(int(difficulty / 5)):
            randomInventory = choice(
                [healthPots.smallHealing, healthPots.smallHealing, healthPots.smallHealing, healthPots.mediumHealing,
                 healthPots.mediumHealing, weapons.genericSword, weapons.weakSword, weapons.weakSword,
                 healthPots.largeHealing, healthPots.largeHealing])
            #  get a list of random items
            hostileInventory.append(randomInventory)
        hostileWeapon = choice([weapons.weakSword, weapons.weakSword, weapons.genericSword, weapons.longSword])
        hostileName = choice(hostileNames)
        hostiles.append(
            Character(10 * difficulty, int(10 * difficulty / 2), 50 * difficulty, 50 * difficulty, difficulty,
                      hostileInventory, False, False, hostileWeapon, True, hostileName,
                      randint(0, (difficulty + 2) ^ 3)))
    return hostiles


class sideCharacters:
    Xavier = Character(100, 100, 100, 100, 100, [healthPots.largeHealing, healthPots.mediumHealing], True, False,
                       Weapon(20, 10), True, "Xavier", 200)
    Boss = Character(1000,1000,1000,1000,20,[weapons.swordOfOrth, weapons.swordOfOrth, healthPots.healthOfOrth, healthPots.healthOfOrth], False, False, weapons.longSword, True, "Top G", 1000)


def navigateMirrorWorld(MainCharacter: Character):
    pos = position(0, 0, 0)

    def movForward():
        if pos.facing == 0:
            try:
                pos.y += 1
                displayImage(mirrorWorldMap[pos.y][pos.x][pos.facing])
            except:
                pos.y = 0
                displayImage(mirrorWorldMap[pos.y][pos.x][pos.facing])
        elif pos.facing == 1:
            try:
                pos.x += 1
                displayImage(mirrorWorldMap[pos.y][pos.x][pos.facing])
            except:
                pos.x = 0
                displayImage(mirrorWorldMap[pos.y][pos.x][pos.facing])
        elif pos.facing == 2:
            try:
                pos.y -= 1
                displayImage(mirrorWorldMap[pos.y][pos.x][pos.facing])
            except:
                pos.y = 0
                displayImage(mirrorWorldMap[pos.y][pos.x][pos.facing])
        elif pos.facing == 3:
            try:
                pos.x -= 1
                displayImage(mirrorWorldMap[pos.y][pos.x][pos.facing])
            except:
                pos.x = 0
                displayImage(mirrorWorldMap[pos.y][pos.x][pos.facing])

        if randint(0, 50) == 1:
            displayImage(imageArray[ImageClass.monster])
            sleep(1)
            imageToAscii.terminalDefault()
            sleep(1)
            battle().start(MainCharacter, *pickRandomHostiles(3, 2), MainCharacter, sideCharacters.Xavier)

    def turnLeft():
        try:
            pos.facing -= 1
            displayImage(mirrorWorldMap[pos.y][pos.x][pos.facing])
        except:
            pos.facing = 3
            displayImage(mirrorWorldMap[pos.y][pos.x][pos.facing])
        if randint(0, 50) == 1:
            displayImage(imageArray[ImageClass.monster])
            sleep(1)
            battle().start(MainCharacter, *pickRandomHostiles(3, 2), MainCharacter, sideCharacters.Xavier)

    def turnRight():
        try:
            pos.facing += 1
            displayImage(mirrorWorldMap[pos.y][pos.x][pos.facing])
        except:
            pos.facing = 0
            displayImage(mirrorWorldMap[pos.y][pos.x][pos.facing])
        if randint(0, 50) == 1:
            displayImage(imageArray[ImageClass.monster])
            sleep(1)
            battle().start(MainCharacter, *pickRandomHostiles(3, 2), MainCharacter, sideCharacters.Xavier)

    displayImage(mirrorWorldMap[pos.y][pos.x][pos.facing])

    while True:
        while True:
            if keyboard.is_pressed('up'):
                movForward()
                pogLog(f"x: {pos.x}, y: {pos.y}, facing: {pos.facing}, moved forward from previous\n")
                sleep(0.5)
                break
            elif keyboard.is_pressed('left'):
                turnLeft()
                pogLog(f"x: {pos.x}, y: {pos.y}, facing: {pos.facing}, turned left from previous\n")
                sleep(0.5)
                break
            elif keyboard.is_pressed('right'):
                turnRight()
                pogLog(f"x: {pos.x}, y: {pos.y}, facing: {pos.facing}, turned right from previous\n")
                sleep(0.5)
                break


def home(MainCharacter: Character):
    INPUT = input("Do you want to go to the \n\
0 :: Fridge, to maybe eat some food \n\
1 :: Your phone, to play slots \n\
2 :: Sleep \n> ")

    #  fridge
    if INPUT == "0":
        if randint(0, 1) == 1:
            eatSock = input(
                "You go to the fridge and find a musty, 12 week old sock from chippy, do you eat it? (y/n) \n> ")
            if eatSock == 'y':
                if randint(0, 1) == 1:
                    print("Your defense stats were buffed because your immune system was super lucky")
                    MainCharacter.defence += 5
                else:
                    print("Unlucky, you have a cold and your defence was slightly lowered")
                    MainCharacter.defence -= 2
            else:
                print("That might've been a good choice.")
        else:
            print(
                "You just stand and stare at the open fridge like an idiot, did you forget what you were doing or something?")
        home(MainCharacter)
        return

    #  slots
    elif INPUT == "1":
        def pickRandomNumbers():
            numbers = []

            for number in range(3):
                numbers.append(randint(0, 7))

            for i in range(10):
                system('cls')
                print(f"{randint(0, 7)},{randint(0, 7)},{randint(0, 7)}")
                sleep(0.1)
            system('cls')
            print(f"{numbers[0]}, {numbers[1]}, {numbers[2]}")
            return numbers

        def checkSlotNumbers(numbers: list[int]):
            countX = lambda lst, x: lst.count(x)
            for number in numbers:
                if countX(numbers, number) == 2:
                    return 1.5
                elif countX(numbers, number) == 3:
                    return 10.0
                else:
                    return 0.0

        def slots():
            if input("Are you sure (y/n)") != 'y':
                return
            moneyIn = input("How much money do you want to gamble? \n> ")
            try:
                moneyIn = int(moneyIn)
            except:
                print("You have to type a number idiot")
                slots()
                return

            print(
                "To win you have to get 2 or 3 of the same number, 2 of the same returns 1.5x your money, 3 of the same returns 10x")
            wait(2)
            if moneyIn >= MainCharacter.money:
                if input("You don't have enough money for that!!, try again or leave (t/l)\n> ") == 't':
                    slots()
                    return
                else:
                    return
            print(f"You spent ${moneyIn} on slots, you now have ${MainCharacter.money - moneyIn} remaining")
            MainCharacter.money = MainCharacter.money - moneyIn
            wait(2)
            showMoney = lambda MainCharacter : print(f"You now have ${MainCharacter.money}")
            system('cls')
            numbers = pickRandomNumbers()
            result = checkSlotNumbers(numbers)
            wait(2)
            if result == 0:
                print("Unlucky, you lost it all")
                showMoney(MainCharacter)
                wait(2)
            elif result == 1.5:
                print(f"Good job, you won {int(moneyIn * result)}")
                MainCharacter.money += int(moneyIn * result)
                showMoney(MainCharacter)
                wait(2)
            elif result == 10:
                print(f"JACKPOT!!, you won {moneyIn * result}")
                MainCharacter.money += moneyIn * result
                showMoney(MainCharacter)
                wait(2)

        slots()
        home(MainCharacter)
        return

    elif INPUT == "2":
        wait(2)
        print("You decide to go to sleep")
        MainCharacter.HP = MainCharacter.maxHP
        MainCharacter.PP = MainCharacter.maxPP
        wait(2)
        # then you do some funny stuff and find some monsters
        navigateMirrorWorld(MainCharacter)

    #  add bed so that you can go to mirror world and fight some funny bois


def summonBoss(MainCharacter: Character):
    for (index, x) in enumerate(MainCharacter.inventory):
        if x.name == "Strange crystal":
            summonsIndex = index
    try:
        summonsIndex = int(summonsIndex)
    except:
        return
    if MainCharacter.inventory[summonsIndex].count <= 3:
        print(f"You have {MainCharacter.inventory[summonsIndex].count} boss summons, you need 3 to summon a boss.")
        return

    INPUT = input(f"You have {MainCharacter.inventory[summonsIndex].count} boss summons, do you want to summon a bos (y/n)\n> ")
    if INPUT.lower() == 'y':
        print("You place the crystals on the ground in a weird formation, and they start to smoke")
        if battle().start(MainCharacter, sideCharacters.Xavier, sideCharacters.Boss):
            print("You win!")
            wait(5)
            displayImage(imageArray[ImageClass.xavier])
    else:
        print("Ok fair enough")
        wait(2)


def main():
    displayImage(imageArray[ImageClass.dudong])
    sleep(3)
    imageToAscii.terminalDefault()

    currentDay = day(True, False)

    MainCharacter = Character(100, 100, 100, 100, 10, [healthPots.mediumHealing], True, True, weapons.genericSword,
                              True, input("What is your name? "))

    if MainCharacter.name.lower() == "orth":
        MainCharacter.inventory.append(healthPots.healthOfOrth)
        MainCharacter.equippedWeapon = weapons.swordOfOrth
        MainCharacter.money = 10000
        print(f"{col.Fore.RED}ORTH IS BLESSED BY THE HEAVENS")
        MainCharacter.inventory.append(weapons.genericSword)
        MainCharacter.showInventory()
        wait(5)
        while True:
            currentDay.stepDay()
            school(MainCharacter)
            choiceMenu(MainCharacter)

    print(
        "You have recently moved to a new school for study, and you have a free period and decide to go straight to "
        "your dorm.\nYou walk into your dorm and see a student who introduces himself to you as your roommate, Xavier")
    input(f"{col.Fore.YELLOW}Press enter to continue")
    system('cls')
    print("You begin your school day")
    wait(2)

    school(MainCharacter)

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
        sleep(1)
        imageToAscii.terminalDefault()
        print("Battle Starting", end="")
        enemy = Character(100, 100, 100, 100, 10, [healthPots.smallHealing], False, False, weapons.weakSword, True,
                          "enemy dumptruck")
        enemy2 = Character(100, 100, 100, 100, 10, [healthPots.smallHealing], False, False, weapons.weakSword, True,
                           "the enemy")
        friend1 = sideCharacters.Xavier
        wait(2)
        battle().start(MainCharacter, MainCharacter, friend1, enemy, enemy2)

        print("Wow that was crazy. I think that was your first time doing that wasn't it?")
        wait(2)
        print("You did well, to kill those monsters")
        wait(2)
        print("this kind of stuff has been happening for a while now, but only a certain few people")
        wait(2)
        print("have been getting transported in the night to some separate world")
        wait(2)
        print("The bad thing is that if you die there you die in this world as well")
        wait(2)

    # if input("Do you want to leave this weirdo school before something like that happens again? (y/n) ")
    while True:
        currentDay.stepDay()
        school(MainCharacter)
        choiceMenu(MainCharacter)
        # then you go home to sleep and consequently choose yes/no to enter the mirror world !!DONE
        # show a bunch of stuff and walk around in the mirror world, if they see a monster they can fight it !!DONE
        # if they get 3 of the items that monsters drop, they can use them to challenge the big boi boss monster
        # if you beat the boss you can finish the game
        summonBoss(MainCharacter)


if __name__ == "__main__":
    main()
    imageToAscii.terminalDefault()

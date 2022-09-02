from typing import List
import colorama as col
import imageToAscii
from time import sleep
from random import randint, choice
from os import system
from time import time
from itertools import zip_longest
from winsound import Beep

col.init(autoreset=True)


class ImageClass:
    xavier = 0
    dudong = 1
    night = 2
    monster = 3


musicNotes = {"C": 262, "D": 294, "E": 330, "F": 349, "G": 392, "A": 440, "B": 494}


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
        elif subject == 1:
            print("You choose to study maths")
            self.music(char)
        elif subject == 2:
            print("You choose to study maths")
            self.maths(char)

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
            if INPUT == noteName:
                print("Good job, you earned 10 health and 10 PP")
                char.maxPP += 10
                char.PP += 10

                char.maxHP += 10
                char.HP += 10
            elif INPUT == "again":
                listen()
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
            if result:
                print("You have defeated all the enemies!")
                earnedItems = []
                for hC in self.hostileCharacters:
                    combinedItems = hC.inventory + [hC.equippedWeapon]
                    for item in combinedItems:
                        if randint(0, 1) == 1:
                            earnedItems.append(item)
                print(f"You gained new items!")
                for i in earnedItems:
                    print(i)
                MainCharacter.inventory.extend(earnedItems)
                return True  # if all enemies are dead return True, a victory
            else:
                pass

    def printBattle(self, friendlyCharacters: List[Character], hostileCharacters: List[Character]):
        for friendlychar, hostilechar in zip_longest(friendlyCharacters, hostileCharacters):
            print(f"""{friendlychar.name} : {friendlychar.HP} {' ' * 20} {hostilechar.name} : {hostilechar.HP}""")


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
                    else:
                        print(
                            f"Insufficient funds, you have {MainCharacter.money}, you need {self.shopInventory[selectedItem][1]}")
                        startOfShop()

            if INPUT == '2':
                print("What do you want to sell?")
                MainCharacter.showInventory()
                selectedItem = input("> ")
                try:
                    selectedItem = int(selectedItem)
                except:
                    print("use a number number idot")
                    startOfShop()

                if len(MainCharacter.inventory) >= selectedItem and selectedItem >= 0:
                    if input(
                            f"Are you sure you want to sell {MainCharacter.inventory[selectedItem]} for {self.getPrice(MainCharacter.inventory[selectedItem])}").lower() == 'y':
                        MainCharacter.money += self.getPrice(MainCharacter.inventory[selectedItem])
                        del MainCharacter.inventory[selectedItem]
                        print("Transaction complete you now have ${}".format(MainCharacter.money))
                        startOfShop()
                    else:
                        startOfShop()
                else:
                    print("You don't have that item idot")
                    startOfShop()
            if INPUT == '3':
                return

        startOfShop()

    def blacksmith(self, MainCharacter: Character):
        pass


def main():
    imageArray = getStoredAscii()

    displayImage(imageArray[ImageClass.dudong])
    sleep(3)
    imageToAscii.terminalDefault()

    currentDay = day(True, False)

    MainCharacter = Character(100, 100, 100, 100, 10, [healthPots.mediumHealing], True, True, weapons.genericSword,
                              True, input("What is your name? "))

    if MainCharacter.name.lower() == "orth":
        MainCharacter.inventory.append(healthPots.healthOfOrth)
        MainCharacter.equippedWeapon = weapons.swordOfOrth
        print(f"{col.Fore.RED}ORTH IS BLESSED BY THE HEAVENS")
        MainCharacter.inventory.append(weapons.genericSword)
        MainCharacter.showInventory()
        wait(5)

    print(
        "You have recently moved to a new school for study, and you have a free period and decide to go straight to "
        "your dorm.\nYou walk into your dorm and see a student who introduces himself to you as your roommate, Xavier")
    input(f"{col.Fore.YELLOW}Press any key to continue")
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
        sleep(0.4)
        imageToAscii.terminalDefault()
        print("Battle Starting", end="")
        enemy = Character(100, 100, 100, 100, 10, [healthPots.smallHealing], False, False, weapons.weakSword, True,
                          "enemy dumptruck")
        enemy2 = Character(100, 100, 100, 100, 10, [healthPots.smallHealing], False, False, weapons.weakSword, True,
                           "the enemy")
        friend1 = Character(100, 100, 100, 100, 100, [], True, False, Weapon(20, 10), True, "Xavier")
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
        #  a choice menu where you decide where you want to go, e.g. the town, straight home, or "sit and admire the scenery", where they watch a rick astley video for a ton of health
        town(MainCharacter)  # a town option where you go to buy stuff from a shop etc.
        # then you go home to sleep and consequently choose yes/no to enter the mirror world
        # show a bunch of stuff and walk around in the mirror world, if they see a monster they can fight it
        # if they get 3 of the items that monsters drop, they can use them to challenge the big boi boss monster
        # if you beat the boss you can finish the game


if __name__ == "__main__":
    main()
    imageToAscii.terminalDefault()

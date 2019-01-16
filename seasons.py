import random

class spring():
    foundShed = False
    location = ''
    passed = ''
    def __init__(self):
        self.passed = False
        self.location = 0
        print('The first door leads you into the Spring Room. You are scared and lost, but at least the weather is nice and the birds are chirping.') 
    
    def start(self):
        self.Q1()
        
    def Q1(self):
        if self.passed: return
        print('''\nChoose your selection:
              R. Explore the River
              F. Explore the Forest
              G. Explore the Garden
              B. Backpack / Check Stats
              ''')
        selection = input()
        choice = newGame.parseText(selection)
        if choice == 'r':
            self.Q2()
        elif choice == 'f':
            self.Q3()
        elif choice == 'g':
            self.Q4(0)
        elif choice != 'b':
            print('Invalid choice')
        self.Q1()
            
    def Q2(self):
        if self.passed: return
        print('\nYou are at the Riverbank') 
        print('''Choose your selection:
              F. Explore the Forest
              G. Explore the Garden
              A. Attempt to fish
              B. Backpack / Check Stats
              ''')
        selection = input()
        choice = newGame.parseText(selection)
        if choice == 'f':
            self.Q3()
        elif choice == 'g':
            self.Q4(0)
        elif choice == 'a':
            event = random.random()
            if (newGame.hand == 'fishing rod' and event < 0.5) or event < 0.2:
                print("You've found a fish!!!!")
                if newGame.foundItem():
                    newGame.getFromGround('fish')
        elif choice != 'b':
            print('Invalid choice')
        self.Q2()
        
    def Q3(self):
        if self.passed: return
        digging = 0
        print('\nYou are in the Forest')
        print('''Choose your selection:
              R. Explore the River
              G. Explore the Garden
              W. Walk Around
              B. Backpack / Check Stats''')
        if newGame.hand == 'shovel':
            print('              D. Dig')
        selection = input()
        choice = newGame.parseText(selection)
        if newGame.hand == 'shovel' and choice == 'd':
            digging += random.random()
            if digging > 0.7:
                if newGame.foundChest():
                    newGame.getFromGround('key')
                    print('key found')
        if choice == 'r':
            self.Q2()
        elif choice == 'g':
            self.Q4(0)
        elif choice != 'b' and choice != 'w' and choice != 'd':
            print('Invalid choice')
        self.Q3()
        
    def Q4(self,e):
        if self.passed: return
        event = random.random()
        if event < 0.1:
            newGame.lives -= 1
            print("Oof, you got stung by a bee and lost one life. Current life: {}".format(newGame.lives))
            e = 0
        event += e
        if event > 1 and not self.foundShed:
            print("You have found the shed, there is a shovel and a fishing rod inside, they might be useful.")
            print('You may use the item that is currently in your hand, ucheck your stats to change the item')
            if newGame.foundItem():
                newGame.getFromGround('shovel')
                newGame.getFromGround('fishing rod')
                self.foundShed = True
            event = 0
        print('You are in the garden')
        print('''Choose your selection:
              R. Explore the River
              F. Explore the Forest
              W. Wander around
              B. Backpack / Check Stats
              ''')
        selection = input()
        choice = newGame.parseText(selection)
        if choice == 'r':
            self.Q2()
        elif choice == 'f':
            self.Q3()
        elif choice != 'b' and choice != 'w':
            print('Invalid choice')
        self.Q4(event)

    def next(self):
        self.passed = True


#####################################################################################################
class summer():
    foundShed = False
    location = ''
    passed = ''
    shells = 0
    def __init__(self):
        self.passed = False
        self.location = 0
        print('You find yourself on a beach, in front of a lemonade stand that appears to sell things beside lemonade.') 
    
    def start(self):
        self.intro()
        
    def intro(self):
        if self.passed: return
        print('''\nChoose your selection:
              L. Explore the lemonade stand
              O. Explore the ocean
              S. Explore the sand
              B. Backpack / Check stats
              ''')
        selection = input()
        choice = newGame.parseText(selection)
        if choice == 'l':
            self.lemonadeStand()
        elif choice == 'o':
            self.ocean()
        elif choice == 's':
            self.sand(0)
        elif choice != 'b':
            print('Invalid choice')
        self.intro()
            
    def lemonadeStand(self):
        if self.passed: return
        print('\nWelcome to the lemonade stand! Here, the currency is shells, which you can find in the ocean.') 
        print('''Choose your selection:
              O. Explore the ocean
              S. Explore the sand
              B. Backpack / Check stats
              D. Browse the item directory
              ''')
        selection = input()
        choice = newGame.parseText(selection)
        if choice == 'd':
            self.directory()
        elif choice == 'o':
            self.ocean()
        elif choice == 's':
            self.sand()
        elif choice != 'b':
            print('Invalid choice')
        self.lemonadeStand()

    def ocean(self):
        if self.passed: return
        print('''Choose your selection:
              L. Explore the lemonade stand
              S. Explore the sand
              B. Backpack / Check stats
              D. Dig for shells by hand
              ''')
        if newGame.hand == 'net':
            print('\t\t N. Use net to look for a pearl')
        selection = input()
        choice = newGame.parseText(selection)
        if choice == 'd':
            digging += random.random()
            if digging > 0.7:
                print('You found a shell!')
                if (true):
                    newGame.getFromGround('shell')
            else:
                print('Sorry, you didn\'t find anything.')
        elif choice == 'l':
            self.lemonadeStand()
        elif choice == 's' and newGame.hand == 'shovel':
            self.sand()
        elif choice == 'n':
            self.net()
        elif choice != 'b':
            print('Invalid choice')
            

        selection = input()
        choice = newGame.parseText(selection)
        if newGame.hand == 'shovel' and choice == 'd':
            digging += random.random()
            if digging > 0.7:
                if newGame.foundChest():
                    newGame.getFromGround('key')
                    print('key found')
        if choice == 'r':
            self.Q2()
        elif choice == 'g':
            self.Q4(0)
        elif choice != 'b' and choice != 'w' and choice != 'd':
            print('Invalid choice')
        self.ocean()

    def sand(self):
        if self.passed: return
        digging = 0
        print('\nItem directory')
        print('''Choose your selection:
              L. Explore the lemonade stand
              O. Explore the ocean
              B. Backpack / Check stats''')
        if newGame.hand == 'metal detector':
            print('              M. Use metal detector')
        selection = input()
        choice = newGame.parseText(selection)
        if newGame.hand == 'metal detector' and choice == 'm':
            detect += random.random()
            if detect > 0.7:
                if newGame.foundChest():
                    pass
                    ############
        if choice == 'l':
            self.lemonadeStand()
        elif choice == 'o':
            self.ocean()
        elif choice != 'b':
            print('Invalid choice')
        self.sand()

    def directory(self):
        if self.passed: return
        digging = 0
        print('\nItem directory')
        print('''What do you want to buy?
              M. Metal detector  1 shell
              L. Lemonade        100 shells
              O. Orangeade       100 shells
              K. Key limeade     100 shells
              C. Cancel''')
        selection = input()
        choice = newGame.parseText(selection)
        if shells >= 1 and choice == 'm':
            shells -= 1
            newGame.getFromGround('metal detector')
        if choice == 'c':
            self.lemonadeStand()
        elif choice != 'b':
            print('Invalid choice')
        self.directory()
    
    def dig(self,e):
        ######
        if self.passed: return
        event = random.random()
        if event < 0.1:
            newGame.lives -= 1
            print("Oof, you got stung by a bee and lost one life. Current life: {}".format(newGame.lives))
            e = 0
        event += e
        if event > 1 and not self.foundShed:
            print("You have found the shed, there is a shovel and a fishing rod inside, they might be useful.")
            print('You may use the item that is currently in your hand, check your stats to change the item')
            if newGame.foundItem():
                newGame.getFromGround('shovel')
                newGame.getFromGround('fishing rod')
                self.foundShed = True
            event = 0
        print('You are in the garden')
        print('''Choose your selection:
              R. Explore the River
              F. Explore the Forest
              W. Wander around
              B. Backpack / Check Stats
              ''')
        selection = input()
        choice = newGame.parseText(selection)
        if choice == 'r':
            self.Q2()
        elif choice == 'f':
            self.Q3()
        elif choice != 'b' and choice != 'w':
            print('Invalid choice')
        self.Q4(event)

    def next(self):
        self.passed = True
##########################################################################################################


class fall():
    passed = ''
    foundRake = False
    foundKey = False
    def __init__(self):
        self.passed = False
    
    def start(self):
        self.Q1()

    def Q1(self):
        if self.passed: return
        print('''\nChoose your selection:
              P. Explore the Pumpkin Patch
              O. Explore the Orchard
              L. Explore the Leaf Pile
              B. Backpack / Check Stats
              ''')
        selection = input()
        choice = newGame.parseText(selection)
        if choice == 'p':
            self.Q2()
        elif choice == 'o':
            self.Q3()
        elif choice == 'l':
            self.Q4()
        elif choice != 'b':
            print('Invalid choice')
        self.Q1()

    def Q2(self):
        pass
    
    def Q3(self):
        if self.passed: return
        print('''\nChoose your selection:
              P. Explore the Pumpkin Patch
              L. Explore the Leaf Pile
              T. Talk to store owner
              W. Walk around
              B. Backpack / Check Stats
              ''')
        selection = input()
        choice = newGame.parseText(selection)
        if choice == 'p':
            self.Q2()
        elif choice == 'l':
            self.Q4()
        elif choice == 't':
            self.Q5()
        elif choice == 'w':
            event = random.random()
            if event < 0.2:
                print('You\'ve found a rotten apple')
                if newGame.foundItem():
                    newGame.getFromGround('rotten apple')
            elif event < 0.4:
                print('You\'ve found an apple')
                if newGame.foundItem():
                    newGame.getFromGround('apple')
            elif event < 0.7:
                print('You\'ve found an knife')
                if newGame.foundItem():
                    newGame.getFromGround('knife')
        elif choice != 'b':
            print('Invalid choice')
        self.Q3()
    
    def Q4(self):
        if not self.foundRake:
            event = random.random()
            if event < 0.25:
                print('You\'ve found a red leaf')
                if newGame.foundItem():
                    newGame.getFromGround('red leaf')
            elif event < 0.5:
                print('You\'ve found a orange leaf')
                if newGame.foundItem():
                    newGame.getFromGround('orange leaf')
            elif event < 0.75:
                print('You\'ve found a yellow leaf')
                if newGame.foundItem():
                    newGame.getFromGround('yellow leaf')
            else:
                print('You\'ve found a green leaf')
                if newGame.foundItem():
                    newGame.getFromGround('green leaf')
        else:
            print('You\'ve found a chest')
            if not self.foundKey:
                print('But you can\'t unlock it')
            else:
                if newGame.foundChest():
                    newGame.getFromGround('key')
                    print('key found')

    def Q5(self):
        print('''Hello! What can I do for you today?
            D. Discuss Deal
            L. Leave Store''')
        selection = input()
        choice = newGame.parseText(selection)
        if choice == 'd':
            if not self.foundRake:
                print('I\'m currently selling a rake for one red leaf, one orange leaf, one yellow leaf, and one green leaf')
                leafCounter = 0
                if (newGame.hand == 'red leaf' or 'red leaf' in newGame.backpack): leafCounter += 1
                if (newGame.hand == 'orange leaf' or 'orange leaf' in newGame.backpack): leafCounter += 1
                if (newGame.hand == 'yellow leaf' or 'yellow leaf' in newGame.backpack): leafCounter += 1
                if (newGame.hand == 'green leaf' or 'green leaf' in newGame.backpack): leafCounter += 1
                if leafCounter == 4:
                    print('             T. Trade')
                    selection = input()
                    choice = newGame.parseText(selection)
                    if choice == 't':
                        newGame.remove('red leaf')
                        newGame.remove('orange leaf')
                        newGame.remove('yellow leaf')
                        newGame.remove('green leaf')
                        newGame.getFromGround('rake')
                        self.foundRake = True
            else:
                print('Sorry, there are no deals today.')
        if choice == 'l':
            print('Thank you for visiting, have a great day!')
        self.Q3()

    def next(self):
        self.passed = True

class game():
    stage = ''
    items = {'':0000,'apple':1, 'fish':2, 'cake':2, 'shovel': 10, 'fishing rod': 11, 'key':100}
    backpack = []
    lives = 5
    hand = ''
    level = 0
    places = [{'r':1, 'f':2, 'g':3},
              {'l':1, 'o':2, 's':3},
              {'p':1, 'l':2, 'x':3},
              {'m':1, 'i':2, 'c':3}]
    location = ''
    def __init__(self):
        print("Hello! You are stuck in the house of a Pinterest mom, where each room is seasonally themed.\n Unfortunately, some of her decorations might be too realistic. Your goal is to make it out of all four rooms alive.")
        print("You have 5 health points, 3 backpack slots, and 1 hand item.")
    def start(self):
        #self.stage = spring()
        #self.stage.start()
        self.stage = fall()
        self.stage.start()
        #self.stage = summer()
        #self.stage.start()
    def getFromBackpack(self, item):
        if item in self.backpack:
            self.backpack.remove(item)
            self.backpack.append(self.hand)
            self.hand = item
        else:
            print("Sorry, there is no such item in your backpack.")
    
    def getFromGround(self, item):
        if len(self.backpack) < 3:
            if self.hand != '':
                self.backpack.append(self.hand)
            self.hand = item
        else:
            print("Sorry, your backpack is full.")

    def remove(self, item):
        if item == self.hand:
            self.hand = ''
        elif item in self.backpack:
            self.backpack.remove(item)

    def useItem(self, item):
        function = self.items[item]
        if len(str(function)) == 1:
            self.lives += function
            if self.lives > 5: 
                self.lives = 5
        elif len(str(function)) == 3:
            self.stage.next()

    def parseText(self, text):
        text = text.lower().strip()
        if text == "b":
            print("lives: " + str(self.lives))
            print("item in hand: " + self.hand)
            print('backpack:' + str(self.backpack)[1:-1])
            self.backpackPrompt()
        elif text in self.places[self.level] and text != self.location:
            self.location = text
            print("You have now changed locations. ")
            return self.location
        return text

    def foundItem(self):
        print('''Choose your selection:
              P. Pick Up
              I. Ignore
              B. Backpack / Check Stats
              ''')
        selection = input()
        choice = self.parseText(selection)
        if choice == 'p':
            return True
        else:
            return False
    
    def foundChest(self):
        print('You\'ve found a chest')
        print('''Choose your selection:
              O. Open Chest
              I. Ignore
              B. Backpack / Check Stats
              ''')
        selection = input()
        choice = self.parseText(selection)
        if choice == 'o':   
            return True
        else:
            return False
    
    def backpackPrompt(self):
        print('Choose your selection:')
        if len(str(self.items[self.hand])) != 2:
            print('          U. Use Item')
        print('''           S. Switch Item
        R. Remove
        C. Cancel
        ''')
        selection = input()
        choice = self.parseText(selection)
        if choice =='u':
            self.useItem(self.hand)
        if choice == 's':
            print('backpack:' + str(self.backpack)[1:-1])
            print('Select an item to switch')
            selection = input()
            self.getFromBackpack(self.parseText(selection))
        elif choice == 'r':
            print('backpack:' + str(self.backpack)[1:-1])
            print('Select an item to remove')
            selection = input()
            self.getFromBackpack(self.remove(selection))

newGame = game()
newGame.start()

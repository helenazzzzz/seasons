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
        choice = game.parseText(newGame,selection)
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
        choice = game.parseText(newGame,selection)
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
        choice = game.parseText(newGame,selection)
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
        choice = game.parseText(newGame,selection)
        if choice == 'r':
            self.Q2()
        elif choice == 'f':
            self.Q3()
        elif choice != 'b' and choice != 'w':
            print('Invalid choice')
        self.Q4(event)

    def next(self):
        self.passed = True

class fall():
    passed = ''
    def __init__(self):
        self.passed = False
    def Q1(self):
        if self.passed: return
        print('''\nChoose your selection:
              P. Explore the Pumpkin Patch
              O. Explore the Orchard
              L. Explore the Leaf Pile
              B. Backpack / Check Stats
              ''')
        selection = input()
        choice = game.parseText(newGame,selection)
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
        pass
    
    def Q4(self):
        pass

class game():
    stage = ''
    items = {'':0000,'apple':1, 'fish':2, 'cake':2, 'shovel': 10, 'fishing rod': 11, 'key':100}
    backpack = []
    lives = 5
    hand = ''
    level = 0
    places = [{'r':1, 'f':2, 'g':3},
              {'s':1, 'o':2, 'b':3},
              {'p':1, 'l':2, 'x':3},
              {'m':1, 'i':2, 'c':3}]
    location = ''
    def __init__(self):
        self.location = 'default_0'
        print("Hello! You are stuck in the house of a Pinterest mom, where each room is seasonally themed.\n Unfortunately, some of her decorations might be too realistic. Your goal is to make it out of all four rooms alive.")
        print("You have 5 health points, 3 backpack slots, and 1 hand item.")
    def start(self):
        self.stage = spring()
        self.stage.start()
        self.stage = fall()
        self.stage.start()
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
            print('What do you want to replace the ' + item + ' in your hand?')
            item = input().lower()
            self.hand = item
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

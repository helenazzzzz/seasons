import random
print("Hello! You are stuck in the house of a Pinterest mom, where each room is seasonally themed.\n Unfortunately, some of her decorations might be too realistic. Your goal is to make it out of all four rooms alive.")
print("You have 5 health points, 3 backpack slots, and 1 hand item.")


class spring():

    foundShed = False
    location = ''
    passed = ''
    def __init__(self):
        self.passed = False
        self.location = 0
        print('The first door leads you into the Spring Room. You are scared and lost, but at least the weather is nice and the birds are chirping.') 
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
              A. Go near the River
              B. Backpack / Check Stats
              ''')
        selection = input()
        choice = game.parseText(newGame,selection)
        if choice == 'f':
            self.Q3()
        elif choice == 'g':
            self.Q4(0)
        elif choice == 'a':
            self.Q5()
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
              B. Backpack / Check Stats
              ''')
        if newGame.hand == 'shovel':
            print('D. Dig')
        selection = input()
        choice = game.parseText(newGame,selection)
        if newGame.hand == 'shovel' and choice == 'd':
            digging += random.random()
            if digging > 0.7:
                if newGame.foundChest():
                    print('key found')
                    self.passed = True
        if choice == 'r':
            self.Q2()
        elif choice == 'g':
            self.Q4(0)
        elif choice != 'b' and choice != 'w':
            print('Invalid choice')
        self.Q3()
        
    def Q4(self,e):
        if self.passed: return
        event = random.random()
        if event < 0.1:
            newGame.lives -= 1
            print("Oof, you've lost one life. Current life: {}".format(newGame.lives))
            e = 0
        event += e
        if event > 1 and not self.foundShed:
            print("You have found the shed, there is a shovel and a fishing rod inside, they might be useful.")
            if newGame.foundItem():
                newGame.getFromGround('shovel')
                newGame.getFromGround('fishing rod')
                self.foundShed = True
            event = 0
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
            
    def Q5(self):
        if self.passed: return
        print('''Choose your selection:
              L. Leave the River
              A. Attempt to fish
              B. Backpack / Check Stats
              ''')
        selection = input()
        choice = game.parseText(newGame,selection)
        if choice == 'l':
            self.Q2()
        elif choice == 'a':
            event = random.random()
            if (newGame.hand == 'fishing rod' and event < 0.5) or event < 0.2:
                print("You've found a fish!!!!")
                if newGame.foundItem():
                    newGame.getFromGround('fish')
        self.Q5()

class game():
    backpack = []
    lives = 5
    items = 0
    hand = ''
    level = 0
    places = [{'r':1, 'f':2, 'g':3},
              {'s':1, 'o':2, 'b':3},
              {'p':1, 'l':2, 'x':3},
              {'m':1, 'i':2, 'c':3}]
    location = ''
    def __init__(self):
        self.location = 'default_0'
    def start(self):
        stage1 = spring()
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
        pass
    
    def parseText(self, text):
        text = text.lower()
        if text == "b":
            print("lives: " + str(self.lives))
            print("item in hand: " + self.hand)
            print('backpack:' + str(self.backpack)[1:-1])
        elif text in self.places[self.level] and text != self.location:
            self.location = text
            print("You have now changed locations. " + self.location)
            return self.location
        return text

    def foundItem(self):
        print('''Choose your selection:
              P. Pick Up
              I. Ignore
              B. Backpack / Check Stats
              ''')
        selection = input()
        choice = game.parseText(newGame,selection)
        if choice == 'p':
            return True
        else:
            return False
    
    def foundChest(self):
        print('''Choose your selection:
              O. Open Chest
              I. Ignore
              B. Backpack / Check Stats
              ''')
        selection = input()
        choice = game.parseText(newGame,selection)
        if choice == 'o':
            pass
        else:
            return

newGame = game()
newGame.start()

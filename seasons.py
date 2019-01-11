print("Hello! You are stuck in the house of a Pinterest mom, where each room is seasonally themed.\n Unfortunately, some of her decorations might be too realistic. Your goal is to make it out of all four rooms alive.")
print("You have 5 health points, 3 backpack slots, and 1 hand item.")
print("drop, take, and use")

class spring():

    location = ''
    passed = ''
    def __init__(self):
        self.passed = False
        self.location = 0
        self.Q1()
    def Q1(self):
        print('The first door leads you into the Spring Room. You are scared and lost, but at least the weather is nice and the birds are chirping.') 
        print('''Choose your selection:
              R. Explore the River
              F. Explore the Forest
              G. Explore the Garden
              B. Backpack / Check Stats
              ''')
        selection = input()
        game.parseText(game,selection)
    def Q2(self):
        print('You are at the River') 
        print('''Choose your selection:
              F. Explore the Forest
              G. Explore the Garden
              A. Go in the River
              W. Walk Around
              B. Backpack / Check Stats
              ''')
        selection = input()
        game.parseText(game,selection)
    def Q3(self):
        print('You are in the Forest')
        print('''Choose your selection:
              R. Explore the River
              G. Explore the Garden
              W. Walk Around
              B. Backpack / Check Stats
              ''')
        selection = input()
        game.parseText(game,selection)
    def Q4(self):
        print('''Choose your selection:
              R. Explore the River
              F. Explore the Forest
              B. Backpack / Check Stats
              ''')
        selection = input()
        game.parseText(game,selection)
    def Q5(self):
        print('''Choose your selection:
              L. Leave the River
              A. Attempt to fish
              B. Backpack / Check Stats
              ''')
    def Q6(self):
        print('''Choose your selection:
              O. Open Chest
              I. Ignore
              B. Backpack / Check Stats
              ''')
    def Q7(self):
        print('''Choose your selection:
              P. Pick Up
              I. Ignore
              B. Backpack / Check Stats
              ''')
    

class game():
    backpack = ['backpack']
    lives = 5
    items = 0
    hand = 'hand'
    level = 0
    places = [{'r':1, 'f':2, 'g':3},
              {'s':1, 'o':2, 'b':3},
              {'p':1, 'l':2, 'x':3},
              {'m':1, 'i':2, 'c':3}]
    location = ''
    def __init__(self):
        self.backpack = []
        self.location = 'default_0'
        stage1 = spring()
        print (stage1.txt)
    def getFromBackpack(self, item):
        if item in self.backpack:
            self.backpack.remove(item)
            self.backpack.append(self.hand)
            self.hand = item
    
    def getFromGround(self, item):
        if len(self.backpack) < 3:
            self.backpack.append(self.hand)
            self.hand = item

    def remove(self, item):
        pass

    def useItem(self, item):
        pass
    
    def parseText(self,text):
        text = text.lower()
        if text == "b":
            print("lives: " + str(self.lives))
            print("item in hand: " + self.hand)
            print("backpack: " + str(self.backpack)[1:-1])
        elif text in self.places[self.level] and text != self.location:
            self.location = text
            print("You have now changed locations. " + self.location)
        elif text in self.places[self.level]:
            print("You are already there. " + self.location)
        else:
            print("Sorry, we didn't get that. Please try again.")


def main():
    newGame = game()
    newGame.getFromBackpack('key')
    print(newGame.hand)

main()


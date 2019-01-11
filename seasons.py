print("Hello! You are stuck in the house of a Pinterest mom, where each room is seasonally themed.\n Unfortunately, some of her decorations might be too realistic. Your goal is to make it out of all four rooms alive.")
print("You have 5 health points, 3 backpack slots, and 1 hand item.")
print("drop, take, and use")

class spring():

    passed = ''
    def __init__(self):
        passed = False
        self.Q1()
    def Q1(self):
        print('''Choose your selection:
              R. Explore the River
              F. Explore the Forest
              G. Explore the Garden
              ''')
        selection = input()
        game.parseText(game,selection)
    def Q2(self):
        pass
    def Q3(self):
        pass
    def Q4(self):
        pass
    def Q5(self):
        pass
    def Q6(self):
        pass

class game():
    backpack = ['','','']
    lives = 5
    items = 0
    hand = ''
    location = 0
    level = 0
    places = [{'r':1, 'f':2, 'g':3},
              {'s':1, 'o':2, 'b':3},
              {'p':1, 'l':2, 'x':3},
              {'m':1, 'i':2, 'c':3},]
    location = ''
    def __init__(self):
        self.backpack = ['','','']
        self.location = 'default_0'
        stage1 = spring()
        
    def getFromBackpack(self, item):
        pass
    
    def getFromGround(self, item):
        pass

    def putInBackpack(self, item):
        pass

    def remove(self, item):
        pass

    def useItem(self, item):
        pass
    def parseText(self,text):
        text = text.lower()
        if text == "b":
            print("lives: " + lives)
            print("item in hand: " + hand)
            print("backpack: " + backpack)
        elif text in places[level] and text != location:
            location = text
            print("You have now changed locations. " + location)
        elif text in places[level]:
            print("You are already there. " + location)
        else:
            print("Sorry, we didn't get that. Please try again. The only text commands are 'drop', 'take', and '


def main():
    newGame = game()
    print(newGame.backpack[0])
    newGame.parseText('take ?')
main()


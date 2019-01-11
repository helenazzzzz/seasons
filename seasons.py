print("Hello! You are stuck in the house of a Pinterest mom, where each room is seasonally themed.\n Unfortunately, some of her decorations might be too realistic. Your goal is to make it out of all four rooms alive.")
print("You have 5 health points, 3 backpack slots, and 1 hand item.")
print("drop, take, and use")

class room():
    
    stage = ''
    level = ''
    passed = False
    def __init__(self, stage, level):
        self.stage = stage
        self.level = level
        print('STAGE {}: {}'.format(self.level+1, self.stage))
        self.play()
    def question(self,scene,qSet):
        choices = len(qSet)
        print(scene)
        print(qSet[0])
        for i in range(1,choices):
            print(qSet[i])
        print('B. Backpack and Stats')
        selection = input()
        game.parseText(game,selection)
    def play(self):
        while not self.passed:
            self.question(scenes[self.level][0],questionBank[self.level][0])

class game():
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
        self.backpack = ['','','']
        self.location = 'default_0'
        stage1 = room('SPRING',0)
        stage2 = room('SUMMER',1)
        stage3 = room('FALL',2)
        stage4 = room('WINTER',3)
        
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
        elif text in places[level] and text not == location:
            location = text
            print("You have now changed locations.")
        elif text in places[level]:
            print("You are already there.")
        else:
            print("Sorry, we didn't get that. Please try again. The only text commands are 'drop', 'take', and 'use'.")

    
        
questionBank = [
    [
        ['Choose your selection',
         'R. Explore the River',
         'F. Explore the Forest',
         'G. Explore the Garden'],
        ],
    [
        ],
    [
        ],
    [
        ]
    ]
scenes = [
    [
       '' 
        ]
    ]

def main():
    newGame = game()
    print(newGame.backpack[0])
    newGame.parseText('take ?')
main()

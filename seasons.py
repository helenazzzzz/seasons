print("Hello! You are stuck in the house of a Pinterest mom, where each room is seasonally themed.\n Unfortunately, some of her decorations might be too realistic. Your goal is to make it out of all four rooms alive.")
print("You have 5 health points, 3 backpack slots, and 1 hand item.")
print("drop, take, and use")

class player():
    backpack = ['','','']
    lives = 5
    items = 0
    hand = ''
    def __init__(self):
        pass
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
    def parseText(text):
        text = text.lower()
        if text == "check stats":
            pass
        elif "drop " in text:
            item = text[5:]
            remove(item)
        elif "take " in text:
            item = text[5:]
            if item in backpack:
                pass
        elif "use " in text:
            item = text[4:]
        else:
            print("Sorry, we didn't get that. Please try again. The only text commands are 'drop', 'take', and 'use'.")
    backpack[0] = '?'
    parseText('take ?')


class room():

    self.passed = False
    
    def __init__(self, stage):
        self.stage = stage

    def question(self,scene,qSet):
        choices = len(qSet)
        print(scene)
        print(qSet[0])
        for i in range(1,choices):
            print('{}. {}'.format(i,qSet[i]))
        print('{}. Use Item'.format(choices))
        print('{}. Drop Item'.format(choices+1))
        print('{}. Check Backpack'.format(choices+2))
        print('{}. Skip Turn'.format(choices+3))
        selection = input()
    def play(self,level):
        while not self.passed:
            self.question(level,question_bank[level][0])

class spring(room):
    def __init__(self, stage = 'spring'):
        super().__init__(stage)
        print('STAGE 1: SPRING')
    play(0)

class summer(room):
    def __init__(self, stage = 'summer'):
        super().__init__(stage)
        print('STAGE 2: SUMMER')

class fall(room):
    def __init__(self, stage = 'fall'):
        super().__init__(stage)
        print('STAGE 3: FALL')

class winter(room):
    def __init__(self, stage = 'winter'):
        super().__init__(stage)
        print('STAGE 4: WINTER')

class game():

    self.questionBank = [
        [
            ['Choose your selection',
             'Explore the River',
             'Explore the Forest',
             'Explore the Garden'],
            
            ],
        [
            ],
        [
            ],
        [
            ]
        ]
    self.scenes = [
            [
               [
                   ]
               ]
        ]
    
    def __init__(self):
        me = player()
        stage1 = spring()

#winter -

def main():
    newGame = game()
    
main()

print("Hello! You are stuck in the house of a Pinterest mom, where each room is seasonally themed.\n Unfortunately, some of her decorations might be too realistic. Your goal is to make it out of all four rooms alive.")
print("You have 5 health points, 3 backpack slots, and 1 hand item.")
print("drop, take, and use")

class player():
    def __init__(self):
        self.backpack = ['','','']
        self.lives = 5
        self.items = 0
        self.hand = ''
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
        if text == "check stats":
            pass
        elif text.contains("drop "):
            item = text[5:]
            remove(item)
        elif text.contains("take "):
            item = text[5:]
        elif text.contains("use "):
            item = text[4:]
        else:
            print("Sorry, we didn't get that. Please try again. The only text commands are 'drop', 'take', and 'use'.")



class room():
    def __init__(self, stage):
        self.stage = stage

    def question(self):
        pass

class spring(room):
    def __init__(self, stage = 'spring'):
        super().__init__(stage)
        print('STAGE 1: SPRING')

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
            ['What do you do?',
             '1. Explore the River',
             '',
             '',
             '']
            
            ]
        [
            ]
        [
            ]
        [
            ]
        ]
    
    def __init__(self):
        me = player()
        stage4 = winter()

#winter -

def main():
    newGame = game()
    
main()

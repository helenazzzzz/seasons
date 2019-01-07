print("Hello! You are an alien from Neptune, and you want to learn more about Earthen seasons.\nYou have signed up for stuff.")

#selena's section ---

#helena's section ---
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
    def __init__(self):
        me = player()
        stage4 = winter()

#winter -

def main():
    newGame = game()
    
main()

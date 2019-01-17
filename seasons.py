import random
import sys

class spring():
    '''
    the spring level
    '''

    foundShed = False       #instance variables that keep track of the player's state in the level
    passed = False

    def __init__(self):
        '''
        the constructor that prints the welcome message for the spring level
        '''
        print('The first door leads you into the Spring Room. You are scared and lost, but at least the weather is nice and the birds are chirping.') 
        
    def start(self):
        '''
        provides a set of choices for the player to choose from and executes the player's desired actions
        '''
        if self.passed: return
        print('+--=====------------------------------------------+')
        print('|                                                 |')
        print('|         0                              XX       |')
        print('|        000             XXXXXX XXXXX   XXXXX     |')
        print('|         0              XXXXXX XXXXX  XXXXXX     |')
        print('|                        XXXXX  XXXXX     X       |')
        print('|                           X     X      XX       |')
        print('|                           X     X               |')
        print('|                                                 |')
        print('|                                              XXXX')
        print('|                                        XXXXXXXXXX')
        print('|       ++ ++ ++                     XXXXXXXXXXXXXX')
        print('|        ++ ++ ++                XXXXXXXXX        |')
        print('|       ++ ++ ++            XXXXXXXX              |')
        print('|        ++ ++ ++        XXXXXXXXX                |')
        print('|                      XXXXXX                     |')
        print('|                   XXXXXXXX                      |')
        print('+--=====----------XXXXXXXXXX----------------------+')        
        print('Choose your selection:')
        print('\t\t R. Explore the River')
        print('\t\t F. Explore the Forest')
        print('\t\t G. Explore the Garden')
        print('\t\t B. Backpack / Check Stats\n')
        selection = input()
        choice = newGame.parseText(selection)
        if choice == 'r':
            self.river()
        elif choice == 'f':
            self.forest()
        elif choice == 'g':
            self.garden(0)
        elif choice != 'b':
            print('Invalid choice')
        self.start()
            
    def river(self):
        '''
        provides a set of choices for the player to choose from and executes the player's desired actions
        the river has a chance where the player could catch fish, determined by the random module
        '''
        if self.passed: return
        print('\nYou are at the Riverbank')
        print('+--=====------------------------------------------+')
        print('|                                                 |')
        print('|                                        XX       |')
        print('|                        XXXXXX XXXXX   XXXXX     |')
        print('|                        XXXXXX XXXXX  XXXXXX     |')
        print('|                        XXXXX  XXXXX     X       |')
        print('|                           X     X      XX       |')
        print('|                           X     X               |')
        print('|                                                 |')
        print('|                                              XXXX')
        print('|                              0         XXXXXXXXXX')
        print('|       ++ ++ ++              000    XXXXXXXXXXXXXX')
        print('|        ++ ++ ++              0 XXXXXXXXX        |')
        print('|       ++ ++ ++            XXXXXXXX              |')
        print('|        ++ ++ ++        XXXXXXXXX                |')
        print('|                      XXXXXX                     |')
        print('|                   XXXXXXXX                      |')
        print('+--=====----------XXXXXXXXXX----------------------+') 
        print('Choose your selection:')
        print('\t\t F. Explore the Forest')
        print('\t\t G. Explore the Garden')
        print('\t\t A. Attempt to fish')
        print('\t\t B. Backpack / Check Stats\n')
        selection = input()
        choice = newGame.parseText(selection)
        if choice == 'f':
            self.forest()
        elif choice == 'g':
            self.garden(0)
        elif choice == 'a':
            event = random.random()
            if (newGame.hand == 'fishing rod' and event < 0.5) or event < 0.2:
                print("You've found a fish!!!!")
                if newGame.foundItem():
                    newGame.getFromGround('fish')
            else:
                print('You didn\'t manage to catch anything')
        elif choice != 'b':
            print('Invalid choice')
        self.river()
        
    def forest(self):
        '''
        provides a set of choices for the player to choose from and executes the player's desired actions
        the forest contains a secret action that could be revealed with an item
        '''
        if self.passed: return
        print('\nYou are in the Forest')
        print('+--=====------------------------------------------+')
        print('|                                                 |')
        print('|                                        XX       |')
        print('|                        XXXXXX XXXXX   XXXXX     |')
        print('|                        XXXXXX XXXXX  XXXXXX     |')
        print('|                        XXXXX  XXXXX 0   X       |')
        print('|                           X     X  000 XX       |')
        print('|                           X     X   0           |')
        print('|                                                 |')
        print('|                                              XXXX')
        print('|                                        XXXXXXXXXX')
        print('|       ++ ++ ++                     XXXXXXXXXXXXXX')
        print('|        ++ ++ ++                XXXXXXXXX        |')
        print('|       ++ ++ ++            XXXXXXXX              |')
        print('|        ++ ++ ++        XXXXXXXXX                |')
        print('|                      XXXXXX                     |')
        print('|                   XXXXXXXX                      |')
        print('+--=====----------XXXXXXXXXX----------------------+') 
        digging = 0
        print('Choose your selection:')
        print('\t\t R. Explore the River')
        print('\t\t G. Explore the Garden')
        print('\t\t W. Walk Around')
        if newGame.hand == 'shovel':
            print('\t\t D. Dig')
        print('\t\t B. Backpack / Check Stats\n')
        selection = input()
        choice = newGame.parseText(selection)
        if newGame.hand == 'shovel' and choice == 'd':
            digging += random.random()
            if digging < 0.4:
                if newGame.foundChest():
                    newGame.getFromGround('key')
                    print('You\'ve found a key')
            else:
                print('You didn\'t manage to dig up anything')
        if choice == 'r':
            self.river()
        elif choice == 'g':
            self.garden(0)
        elif choice != 'b' and choice != 'w' and choice != 'd':
            print('Invalid choice')
        self.forest()
        
    def garden(self,e):
        '''
        provides a set of choices for the player to choose from and executes the player's desired actions
        the garden contains bees that can sting the player
        the player has a chance of encountering a shed, which is determined through the random module and the chance increases as garden() is repeatedly called
        '''
        if self.passed: return
        print('You are in the garden')
        event = random.random()
        if event < 0.1:
            newGame.loseLife(1)
            print("Oof, you got stung by a bee and lost one life. Current life: {}".format(newGame.lives))
            e = 0
        event += e
        if event > 1 and not self.foundShed:
            print("You have found the shed with a shovel and a fishing rod inside. They might be useful.")
            print('You may use the item that is currently in your hand. Check your backpack to change the item.')
            if newGame.foundItem():
                newGame.getFromGround('shovel')
                newGame.getFromGround('fishing rod')
                self.foundShed = True
            event = 0
        print('+--=====------------------------------------------+')
        print('|                                                 |')
        print('|                                        XX       |')
        print('|                        XXXXXX XXXXX   XXXXX     |')
        print('|                        XXXXXX XXXXX  XXXXXX     |')
        print('|                        XXXXX  XXXXX     X       |')
        print('|                           X     X      XX       |')
        print('|                           X     X               |')
        print('|                                                 |')
        print('|         0                                    XXXX')
        print('|        000                             XXXXXXXXXX')
        print('|       ++0++ ++                     XXXXXXXXXXXXXX')
        print('|        ++ ++ ++                XXXXXXXXX        |')
        print('|       ++ ++ ++            XXXXXXXX              |')
        print('|        ++ ++ ++        XXXXXXXXX                |')
        print('|                      XXXXXX                     |')
        print('|                   XXXXXXXX                      |')
        print('+--=====----------XXXXXXXXXX----------------------+') 
        print('Choose your selection:')
        print('\t\t R. Explore the River')
        print('\t\t F. Explore the Forest')
        print('\t\t W. Wander Around')
        print('\t\t B. Backpack / Check Stats\n')
        selection = input()
        choice = newGame.parseText(selection)
        if choice == 'r':
            self.river()
        elif choice == 'f':
            self.forest()
        elif choice != 'b' and choice != 'w':
            print('Invalid choice')
        self.garden(event)



class summer():
    passed = ''
    def __init__(self):
        self.passed = False
        self.foundChest = False
        print('You find yourself on a beach, in front of a lemonade stand that appears to sell things besides lemonade.') 
    
    def start(self):
        self.intro()
        
    def intro(self):
        if self.passed: return
        print('+--=====------------------------------------------+')
        print('|                                                 |')
        print('|                                  XXX            |')
        print('|          0                     XX   XX          |')
        print('|         000                  XX       XX        |')
        print('|          0                   +---------+        |')
        print('|                              |         |        |')
        print('|                              |  +---+  |        |')
        print('|                              +---------+        |')
        print('|                                                 X')
        print('|             ++                                XXX')
        print('|      ++                                    XXXXXX')
        print('|          ++       ++                  XXXXXXXXXXX')
        print('|   ++          ++                   XXXXXXXXXXXXXX')
        print('|        ++           ++           XXXXXXXXXXXXXXXX')
        print('|            ++            XXXXXXXXXXXXXXXXXXXXXXXX')
        print('|                      XXXXXXXXXXXXXXXXXXXXXXXXXXXX')
        print('+--=====-------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
        print('Choose your selection:')
        print('\t\t L. Explore the lemonade stand')
        print('\t\t O. Explore the ocean')
        print('\t\t S. Explore the sand')
        print('\t\t B. Backpack / Check stats\n')
        selection = input()
        choice = newGame.parseText(selection)
        if choice == 'l':
            self.lemonadeStand()
        elif choice == 'o':
            self.ocean()
        elif choice == 's':
            self.sand()
        elif choice != 'b':
            print('Invalid choice')
        self.intro()
            
    def lemonadeStand(self):
        if self.passed: return
        print('\nYou are at the lemonade stand! Here, the currency consists of shells and pearls, which you can find in the ocean.') 
        print('+--=====------------------------------------------+')
        print('|                                                 |')
        print('|                                  XXX            |')
        print('|                                XX   XX          |')
        print('|                              XX       XX        |')
        print('|                              +---------+        |')
        print('|                              |         |        |')
        print('|                              |  +---+  |        |')
        print('|                              +----0----+        |')
        print('|                                  000            X')
        print('|             ++                    0           XXX')
        print('|      ++                                    XXXXXX')
        print('|          ++       ++                  XXXXXXXXXXX')
        print('|   ++          ++                   XXXXXXXXXXXXXX')
        print('|        ++           ++           XXXXXXXXXXXXXXXX')
        print('|            ++            XXXXXXXXXXXXXXXXXXXXXXXX')
        print('|                      XXXXXXXXXXXXXXXXXXXXXXXXXXXX')
        print('+--=====-------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
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
        print('+--=====------------------------------------------+')
        print('|                                                 |')
        print('|                                  XXX            |')
        print('|                                XX   XX          |')
        print('|                              XX       XX        |')
        print('|                              +---------+        |')
        print('|                              |         |        |')
        print('|                              |  +---+  |        |')
        print('|                              +---------+        |')
        print('|                                                 X')
        print('|             ++                                XXX')
        print('|      ++                                    XXXXXX')
        print('|          ++       ++                0 XXXXXXXXXXX')
        print('|   ++          ++                   000XXXXXXXXXXX')
        print('|        ++           ++           XXX0XXXXXXXXXXXX')
        print('|            ++            XXXXXXXXXXXXXXXXXXXXXXXX')
        print('|                      XXXXXXXXXXXXXXXXXXXXXXXXXXXX')
        print('+--=====-------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
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
            digging = random.random()
            if digging > 0.3:
                print('You found a shell!')
                if newGame.foundItem():
                    newGame.getFromGround('shell')
                print('hand: ' + newGame.hand)
                print('backpack: ' + str(newGame.backpack))
            elif digging > 0.5:
                print("Ouch! You've been stung by a jellyfish and lost a life. Current life: {}".format(newGame.lives))
                newGame.lives -= 1
            else:
                print('Sorry, you didn\'t find anything. You might if you tried again, though...')
        elif choice == 'l':
            self.lemonadeStand()
        elif choice == 's':
            self.sand()
        elif choice == 'n':
            print('Congratulations! You found a pearl!')
            if newGame.foundItem():
                newGame.getFromGround('pearl')
        elif choice != 'b':
            print('Invalid choice')
        self.ocean()

    def sand(self):
        if self.passed: return
        print('+--=====------------------------------------------+')
        print('|                                                 |')
        print('|                                  XXX            |')
        print('|                                XX   XX          |')
        print('|                              XX       XX        |')
        print('|                              +---------+        |')
        print('|                              |         |        |')
        print('|                              |  +---+  |        |')
        print('|                              +---------+        |')
        print('|                                                 X')
        print('|             ++0                               XXX')
        print('|      ++      000                           XXXXXX')
        print('|          ++   0   ++                  XXXXXXXXXXX')
        print('|   ++          ++                   XXXXXXXXXXXXXX')
        print('|        ++           ++           XXXXXXXXXXXXXXXX')
        print('|            ++            XXXXXXXXXXXXXXXXXXXXXXXX')
        print('|                      XXXXXXXXXXXXXXXXXXXXXXXXXXXX')
        print('+--=====-------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
        detect = 0
        print('\nItem directory')
        print('Choose your selection:')
        print('\t\t L. Explore the lemonade stand')
        print('\t\t O. Explore the ocean')
        print('\t\t B. Backpack / Check stats')
        if self.foundChest:
            print('\t\t C. Open Chest')
        if newGame.hand == 'metal detector':
            print('\t\t M. Use metal detector')
        selection = input()
        choice = newGame.parseText(selection)
        if newGame.hand == 'metal detector' and choice == 'm' and not(self.foundChest):
            detect += random.random()
            if detect < 0.7:
                self.foundChest = True
                print('The metal detector beeps when you hover over a raised mound of sand. You\'ve found a chest!')
        elif newGame.hand == 'metal detector' and choice == 'm' and (self.foundChest):
            print('The metal detector doesn\'t beep. There\'s nothing metal left on the beach.')
        elif choice == 'l':
            self.lemonadeStand()
        elif choice == 'o':
            self.ocean()
        elif choice != 'b':
            print('Invalid choice')
        self.sand()

    def directory(self):
        if self.passed: return
        print('\nItem directory')
        print('''What do you want to buy?
              M. Metal detector  1 shell
              L. Lemonade        1 pearl
              O. Orangeade       1 pearl
              K. Key limeade     1 pearl
              C. Cancel''')
        selection = input()
        choice = newGame.parseText(selection)
        if ("shell" in newGame.backpack or newGame.hand == 'shell') and choice == 'm':
            newGame.getFromGround('metal detector')
            newGame.remove("shell")
        elif ("pearl" in newGame.backpack or newGame.hand == 'pearl') and choice == 'l':
            newGame.getFromGround('lemonade')
            newGame.remove("pearl")
        elif ("pearl" in newGame.backpack or newGame.hand == 'pearl') and choice == 'o':
            newGame.getFromGround('orangeade')
            newGame.remove("pearl")
        elif ("pearl" in newGame.backpack or newGame.hand == 'pearl') and choice == 'k':
            newGame.getFromGround('limeade')
            print('The key limeade came with a key that you can use to move on to the next level!')
            newGame.getFromGround('key')
            newGame.remove("pearl")
        elif choice == 'c':
            self.lemonadeStand()
        elif choice != 'b':
            print('Invalid choice')
        self.directory()

class fall():
    passed = False     #instance variables that keep track of the player's state in the level
    foundRake = False
    foundKey = False
    foundKnife = False
    foundChest = False
    def __init__(self):
        '''
        the constructor that prints the welcome message for the fall level
        '''
        print('Welcome to the fall room. The weather is getting a little chilly and the air is filled with the rich scents of pumpkin spice latte and apple pie.')

    def start(self):
        '''
        provides a set of choices for the player to choose from and executes the player's desired actions
        '''
        if self.passed: return
        print('+--=====------------------------------------------+')
        print('|                                                 |')
        print('|        0                                        |')
        print('|       000              +-+ +-+ +-+ +-+ +-+ +-+ |')
        print('|        0                | | | | | | | | | | | | |')
        print('|                         +++ +++ +++ +++ +++ +++ |')
        print('|                          |   |   |   |   |   |  |')
        print('|                          +   +   +   +   +   +  |')
        print('|                 X                               |')
        print('|            X                                    |')
        print('|      X  XXX   X                             ++  |')
        print('|    X X XXXXXXXXX       ++         ++        ++  |')
        print('|    X XXXXXXXXXXX      +--+  ++   +--+    ++     |')
        print('|   X  XXXXXXXXXXX       ++  +--+   ++    +--+    |')
        print('|         XXXXXXX X           ++       ++  ++     |')
        print('|            XX                        ++         |')
        print('|                                                 |')
        print('+--=====------------------------------------------+')
        print('Choose your selection:')
        print('\t\t P. Explore the Pumpkin Patch')
        print('\t\t O. Explore the Orchard')
        print('\t\t L. Explore the Leaf Pile')
        print('\t\t B. Backpack / Check Stats\n')
        selection = input()
        choice = newGame.parseText(selection)
        if choice == 'p':
            self.pumpkin()
        elif choice == 'o':
            self.orchard()
        elif choice == 'l':
            self.leaf()
        elif choice != 'b':
            print('Invalid choice')
        self.start()

    def pumpkin(self):
        '''
        provides a set of choices for the player to choose from and executes the player's desired actions
        players may also perform actions with the pumpkins
        '''
        if self.passed: return
        print('You are at the pumpkin patch.')
        print('+--=====------------------------------------------+')
        print('|                                                 |')
        print('|                                                 |')
        print('|                         +-+ +-+ +-+ +-+ +-+ +-+ |')
        print('|                         | | | | | | | | | | | | |')
        print('|                         +++ +++ +++ +++ +++ +++ |')
        print('|                          |   |   |   |   |   |  |')
        print('|                          +   +   +   +   +   +  |')
        print('|                 X                               |')
        print('|            X                                    |')
        print('|      X  XXX   X                        0    ++  |')
        print('|    X X XXXXXXXXX       ++         ++  000   ++  |')
        print('|    X XXXXXXXXXXX      +--+  ++   +--+  0 ++     |')
        print('|   X  XXXXXXXXXXX       ++  +--+   ++    +--+    |')
        print('|         XXXXXXX X           ++       ++  ++     |')
        print('|            XX                        ++         |')
        print('|                                                 |')
        print('+--=====------------------------------------------+')
        print('Choose your selection:')
        print('\t\t O. Explore the Orchard')
        print('\t\t L. Explore the Leaf Pile')
        print('\t\t S. Smash a pumpkin')
        if newGame.hand == 'knife':
            print('\t\t C. Carve a pumpkin')
        print('\t\t B. Backpack / Check Stats\n')
        selection = input()
        choice = newGame.parseText(selection)
        if choice == 'o':
            self.orchard()
        elif choice == 'l':
            self.leaf()
        elif choice == 's':
            print('Oof, you dropped the pumpkin on your feet and man that hurts :\'(. Minus one life')
            newGame.loseLife(1)
        elif choice == 'c' and self.foundKnife:
            event = random.random()
            if event < 0.5:
                print('You\'ve found a key')
                if newGame.foundItem():
                    newGame.getFromGround('a key')
                    self.foundKey = True
        elif choice != 'b':
            print('Invalid choice')
        self.pumpkin()
        
    def orchard(self):
        '''
        provides a set of choices for the player to choose from and executes the player's desired actions
        the orchard contains items which the player can find, determined by the random module
        the player may trade at the store
        '''
        if self.passed: return
        print('You are at the orchard.')
        print('+--=====------------------------------------------+')
        print('|                                                 |')
        print('|                                                 |')
        print('|                         +-+ +-+ +-+ +-+ +-+ +-+ |')
        print('|                         | | | | | | | | | | | | |')
        print('|                     0   +++ +++ +++ +++ +++ +++ |')
        print('|                    000   |   |   |   |   |   |  |')
        print('|                     0    +   +   +   +   +   +  |')
        print('|                 X                               |')
        print('|            X                                    |')
        print('|      X  XXX   X                             ++  |')
        print('|    X X XXXXXXXXX       ++         ++        ++  |')
        print('|    X XXXXXXXXXXX      +--+  ++   +--+    ++     |')
        print('|   X  XXXXXXXXXXX       ++  +--+   ++    +--+    |')
        print('|         XXXXXXX X           ++       ++  ++     |')
        print('|            XX                        ++         |')
        print('|                                                 |')
        print('+--=====------------------------------------------+')
        print('Choose your selection:')
        print('\t\t P. Explore the Pumpkin Patch')
        print('\t\t L. Explore the Leaf Pile')
        print('\t\t T. Talk to store owner')
        print('\t\t W. Walk around')
        print('\t\t B. Backpack / Check Stats\n')
        selection = input()
        choice = newGame.parseText(selection)
        if choice == 'p':
            self.pumpkin()
        elif choice == 'l':
            self.leaf()
        elif choice == 't':
            self.store()
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
            elif event < 0.7 and not self.foundKnife:
                print('You\'ve found an knife')
                if newGame.foundItem():
                    newGame.getFromGround('knife')
                    self.foundKnife = True
        elif choice != 'b':
            print('Invalid choice')
        self.orchard()
    
    def leaf(self):
        '''
        provides a set of choices for the player to choose from and executes the player's desired actions
        the player may collect leaves or perform other actions
        '''
        if self.passed: return
        print('You are at the leaf pile.')
        print('+--=====------------------------------------------+')
        print('|                                                 |')
        print('|                                                 |')
        print('|                         +-+ +-+ +-+ +-+ +-+ +-+ |')
        print('|                         | | | | | | | | | | | | |')
        print('|                         +++ +++ +++ +++ +++ +++ |')
        print('|                          |   |   |   |   |   |  |')
        print('|                          +   +   +   +   +   +  |')
        print('|                 X                               |')
        print('|            X   0                                |')
        print('|      X  XXX   000                           ++  |')
        print('|    X X XXXXXXXX0       ++         ++        ++  |')
        print('|    X XXXXXXXXXXX      +--+  ++   +--+    ++     |')
        print('|   X  XXXXXXXXXXX       ++  +--+   ++    +--+    |')
        print('|         XXXXXXX X           ++       ++  ++     |')
        print('|            XX                        ++         |')
        print('|                                                 |')
        print('+--=====------------------------------------------+')
        print('Choose your selection:')
        print('\t\t P. Explore the Pumpkin Patch')
        print('\t\t O. Explore the Orchard')
        print('\t\t L. Pick up a leaf')
        if newGame.hand == 'rake':
            print('\t\t R. Rake')
        if self.foundChest:
            print('\t\t C. Open Chest')
        print('\t\t B. Backpack / Check Stats\n')
        selection = input()
        choice = newGame.parseText(selection)
        if choice == 'p':
            self.pumpkin()
        elif choice == 'o':
            self.orchard()
        elif choice == 'l':
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
        elif choice == 'r' and newGame.hand == 'rake':
            print('You\'ve found a chest')
            self.foundChest = True
        elif choice == 'c' and self.foundChest:
            if newGame.foundChest():
                if newGame.hand != 'a key':
                    print('But you can\'t unlock it')
                    if self.foundKey:
                        print('Hint: Switch to the key item to unlock the chest')
                else:
                    newGame.remove('a key')
                    newGame.getFromGround('key')
                    print('You\'ve found a key')
        elif choice != 'b':
            print('Invalid choice')
        self.leaf()
            

    def store(self):
        '''
        provides a set of choices for the player to choose from and executes the player's desired actions
        the player can interact and trade with the merchant, the method checks whether the player has the right items to trade
        '''
        print('Hello! What can I do for you today?')
        print('\t\t D. Discuss Deal')
        print('\t\t L. Leave Store')
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
                    print('\t\t T. Trade')
                    print('\t\t C. Cancel')
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
        elif choice != 'l':
            print('Invalid choice')
        print('Thank you for visiting, have a great day!')
        self.orchard()


class winter():
    def __init__(self):
        self.passed = False
        self.foundLamp = False
        print("You have entered the winter room. You're in a cabin, which is dimly lit by the flickering fireplace. Outside it is pitch-black. You wouldn't be able to see anything without a lamp.") 
    
    def start(self):
        self.intro()
        
    def intro(self):
        if self.passed: return
        print('+--=====------------------------------------------+')
        print('|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|')
        print('|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|')
        print('|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|')
        print('|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|')
        print('|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|')
        print('|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|')
        print('|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|')
        print('|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|')
        print('|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|')
        print('|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|')
        print('|XXXXXX  0  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|')
        print('|XXXXXX 000 XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|')
        print('|XXXXXX--0--XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|')
        print('|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|')
        print('|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|')
        print('|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|')
        print('+-------------------------------------------------+')
        print('Choose your selection:')
        print('\t\t C. Explore the cabin')
        print('\t\t W. Wander around outside')
        print('\t\t B. Backpack / Check stats\n')
        selection = input()
        choice = newGame.parseText(selection)
        if choice == 'c':
            self.cabin()
        elif choice == 'w':
            self.wander()
        elif choice != 'b':
            print('Invalid choice')
        self.intro()
            
    def cabin(self):
        if self.passed: return
        print('You are in the cabin. Choose your selection:') 
        print('\t\t C. Explore the cabin')
        if newGame.hand == 'lamp':
            print('\t\t M. Explore the mountain')
            print('\t\t L. Explore the frozen lake')
        print('\t\t B. Backpack / Check stats\n')
        selection = input()
        choice = newGame.parseText(selection)
        if choice == 'c' and self.foundLamp == False:
            print("You've found a lamp on the ground! It's already lit, and when you go near it, it warms your feet.")
            if newGame.foundItem():
                newGame.getFromGround('lamp')
        elif choice == 'c' and self.foundLamp == True:
            print("Hmm, looks like there's nothing new here.")
        elif choice == 'm' and newGame.hand == 'lamp':
            self.mountain()
        elif choice == 'l' and newGame.hand == 'lamp':
            self.lake()
        elif choice != 'b':
            print('Invalid choice')
        self.cabin()

    def wander(self):
        if self.passed: return
        print('+--=====------------------------------------------+')
        print('|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|')
        print('|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|')
        print('|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|')
        print('|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|')
        print('|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|')
        print('|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|')
        print('|XXXXX+------+XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|')
        print('|XXXX+        +xXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|')
        print('|XXX++        ++XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|')
        print('|XXX+----------+XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|')
        print('|XXX|    0     |X0XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|')
        print('|XXX|   000    |000XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|')
        print('|XXX+----0-----+X0XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|')
        print('|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|')
        print('|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|')
        print('|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|')
        print('+-------------------------------------------------+')
        newGame.lives -= 1
        print("Without a source of heat, you feel your hands starting to go numb. That can't be good. You lose a life. Lives: " + str(newGame.lives))
        print("Choose your selection:") 
        print('\t\t C. Go back to the cabin')
        print('\t\t W. Wander more')
        print('\t\t B. Backpack / Check stats\n')
        selection = input()
        choice = newGame.parseText(selection)
        if choice == 'c':
            self.cabin()
        elif choice != 'w' and choice != 'd':
            print('Invalid choice')
        self.wander()

    def lake(self):
        if self.passed: return
        print('+--=====------------------------------------------+')
        print('|                                                 |')
        print('|                               X                 |')
        print('|                              XXX     X          |')
        print('|                              X X    XXX   XXX   |')
        print('|                             X  XX  XX XXXX  XX  |')
        print('|                           XX    XXXX   XX    X  |')
        print('|     +------+             XX      XX     X    XX |')
        print('|    +        +                     XX     XX     |')
        print('|   ++        ++                                  |')
        print('|   +----------+                                  |')
        print('|   |          |                          XXXXXXXXX')
        print('|   |          |                      XXXXXXXXXXXXX')
        print('|   +----------+                 XXX0XXXXXXXXXXXXXX')
        print('|                           XXXXXXX000XXXXXXXXXXXXX')
        print('|                         XXXXXXXXXX0XXXXXXXXXXXXXX')
        print('|                         XXXXXXXXXXXXXXXXXXXXXXXXX')
        print('+--=====-------------------XXXXXXXXXXXXXXXXXXXXXXXX')
        print('You are at the frozen lake. Choose your selection:') 
        print('\t\t C. Explore the cabin')
        print('\t\t M. Explore the mountain')
        print('\t\t W. Walk on top of the lake')
        print('\t\t B. Backpack / Check stats\n')
        selection = input()
        choice = newGame.parseText(selection)
        if choice == 'c':
            self.cabin()
        elif choice == 'm':
            self.mountain()
        elif choice == 'w':
            print("As you walk, you notice something glinting beneath your feet. You bend down and see that it's a key! Unfortunately, it's stuck under the surface of the ice.")
            print("You realize if you want to get out, you need something to get through the ice. You try...")
            print('M. Using your hands to melt the ice')
            print('K. Kicking the ice')
            print('L. Using the lamp')
            for item in newGame.backpack:
                print(item[0].upper() + '. Using the '+ item)
            print('C. Cancel')
            selection = input()
            use = newGame.parseText(selection)
            if use == 'l':
                print("You set down the lamp, and you watch as the flame inside slowly melts the ice! You snatch the key quickly and put it in your backpack.")
                newGame.getFromGround('key')
            elif use == 'p' and 'pickax' in newGame.backpack:
                newGame.loseLife(1)
                print("You try to get the key with the pickax, but it's too far down to reach. Instead, you hurt your shoulder trying break the ice. Lose a life. Lives: " +newGame.lives)
            elif use == 'k':
                print("Ow. Did you really think that would work? You won't lose a life because the pain of stubbing your toe is already bad enough.")
            elif use == 'm':
                newGame.loseLife(1)
                print("Some of the ice melts, but you realize it'll take forever and you'll get frostbite before it works. And what are the symptoms of hypothermia again? Lose a life. Lives: " +newGame.lives)
            elif use != 'c':
                print("This is a great item, but it doesn't help you melt the ice. Maybe try again.")
        elif choice != 'b':
            print('Invalid choice')
        self.lake()

    def mountain(self):
        if self.passed: return
        print('+--=====------------------------------------------+')
        print('|                                                 |')
        print('|                               X                 |')
        print('|                              XXX     X          |')
        print('|                              X X    XXX   XXX   |')
        print('|                             X  XX  XX XXXX  XX  |')
        print('|                           XX    XXXX   XX    X  |')
        print('|     +------+             XX 0    XX     X    XX |')
        print('|    +        +              000    XX     XX     |')
        print('|   ++        ++              0                   |')
        print('|   +----------+                                  |')
        print('|   |          |                          XXXXXXXXX')
        print('|   |          |                      XXXXXXXXXXXXX')
        print('|   +----------+                 XXXXXXXXXXXXXXXXXX')
        print('|                           XXXXXXXXXXXXXXXXXXXXXXX')
        print('|                         XXXXXXXXXXXXXXXXXXXXXXXXX')
        print('|                         XXXXXXXXXXXXXXXXXXXXXXXXX')
        print('+--=====-------------------XXXXXXXXXXXXXXXXXXXXXXXX')
        print('You are in the mountain. Choose your selection:') 
        print('\t\t C. Explore the cabin')
        print('\t\t L. Explore the frozen lake')
        print('\t\t M. Climb the mountain')
        print('\t\t B. Backpack / Check stats\n')
        selection = input()
        choice = newGame.parseText(selection)
        if choice == 'c':
            self.cabin()
        elif choice == 'l':
            self.lake()
        elif choice == 'm':
            findPickax = random.random()
            if findPickax < 0.5:
                print("You climb for a little bit and find nothing, but you might be able to find something if you keep going...")
            else:
                print("You found a pickax!")
                if newGame.foundItem():
                    newGame.getFromGround('pickax')
        elif choice != 'w':
            print('Invalid choice')
        self.mountain()

class game():
    stage = ''                      #instance variables of the game
    items = {'':1000,               #the length of each item's key indicates the item's use
    'rotten apple':0,               #1: food, the number is the amount of lives the player receives, may be used in the backpack
    'apple':1,                      #2: an item that can be used in certain scenario, unusable in the backpack
    'fish':2,                       #3: an item that can be used in the backpack
    'lemonade': 1,
    'limeade': 1,
    'orangeade': 1,
    'shovel': 10, 
    'fishing rod': 11, 
    'rake': 12, 
    'red leaf': 13, 
    'orange leaf': 14, 
    'yellow leaf':15, 
    'green leaf': 16, 
    'knife':17, 
    'shell':18, 
    'pearl':19, 
    'key':100, 
    'a key': 20,
    'metal detector': 21}
    backpack = []
    lives = 5
    hand = ''
    def __init__(self):
        '''
        the constructor that prints the welcome message for the fall level
        '''
        print("Hello! You are stuck in the house of a Pinterest mom, where each room is seasonally themed.\n Unfortunately, some of her decorations might be too realistic. Your goal is to make it out of all four rooms alive.")
        print("You have 5 health points, 3 backpack slots, and 1 hand item.")
    def start(self):
        self.stage = spring()
        self.stage.start()
        print ("Congratulations, you got out of spring alive!! You use the key and enter the summer room...")
        self.stage = summer()
        self.stage.start()
        print ("You made it through summer, too! Now onto fall...")
        self.stage = fall()
        self.stage.start()
        print ("You got through, fall, but winter is coming...")
        self.stage = winter()
        self.stage.start()
        print ("You've won the game!! Congratulations!")
        print('After some hard work, you have finally escaped the house of teh pinterest mom. What do you do after this?? Go on Pinterest of course. Maybe you can decorate your rooms like this too.')
    def getFromBackpack(self, item):
        '''
        exchanges an item in the backack with item in hand
        '''
        if item in self.backpack:
            self.backpack.remove(item)
            self.backpack.append(self.hand)
            self.hand = item
        else:
            print("Sorry, there is no such item in your backpack.")

    def loseLife(self, lost):
        '''
        ends the game when the player has no lives left
        '''
        self.lives -= lost
        if self.lives < 0:
            print('Sorry, you have no more lives left.')
            sys.exit()

    
    def getFromGround(self, item):
        '''
        retrieves an item from ground and replaces item in hand into the backpack
        '''
        if len(self.backpack) < 3:
            if self.hand != '':
                self.backpack.append(self.hand)
            self.hand = item
        else:
            print("Sorry, your backpack is full.")
            print('\t\t R. Remove an Item')
            print('\t\t C. Cancel')
            selection = input()
            choice = self.parseText(selection)
            if choice == 'r':
                print('backpack:' + str(self.backpack)[1:-1])
                print('Select an item to remove')
                selection = input()
                self.remove(selection)
                if self.hand != '':
                    self.backpack.append(self.hand)
                self.hand = item

    def remove(self, item):
        '''
        discard an item
        '''
        if item == self.hand:
            self.hand = ''
        elif item in self.backpack:
            self.backpack.remove(item)

    def useItem(self, item):
        '''
        the item performs its trick and is disposed
        '''
        function = self.items[item]
        if len(str(function)) == 1:
            self.lives += function
            if self.lives > 5: 
                self.lives = 5
        elif len(str(function)) == 3:
            self.nextLevel()

    def parseText(self, text):
        '''
        formats the text for the methods to read and opens backpack and stats
        '''
        text = text.lower().strip()
        if text == "b":
            print("lives: " + str(self.lives))
            print("item in hand: " + self.hand)
            print('backpack:' + str(self.backpack)[1:-1])
            self.backpackPrompt()
        return text

    def foundItem(self):
        '''
        prompt the player to make a decision on an item
        '''
        choice = 'b'
        while choice == 'b':
            print('Choose your selection:')
            print('\t\t P. Pick Up')
            print('\t\t I. Ignore')
            print('\t\t B. Backpack / Check Stats\n')
            selection = input()
            choice = self.parseText(selection)
        if choice == 'p':
            return True
        else:
            return False
    
    def foundChest(self):
        '''
        prompt the player to make a decision on a chest
        '''
        print('You\'ve found a chest')
        choice = 'b'
        while choice == 'b':
            print('Choose your selection:')
            print('\t\t O. Open Chest')
            print('\t\t I. Ignore')
            print('\t\t B. Backpack / Check Stats\n')
            selection = input()
            choice = self.parseText(selection)
        if choice == 'o':   
            return True
        
        else:
            return False
    
    def backpackPrompt(self):
        '''
        prompt the player to make a decision in the backpack
        '''
        print('Choose your selection:')
        if len(str(self.items[self.hand])) % 2 == 1:
            print('\t\t U. Use Item')
        if len(self.backpack) == 0:
            print('\t\t A. Add Item to backpack')
        print('\t\t S. Switch Item')
        print('\t\t R. Remove')
        print('\t\t C. Cancel\n')
        selection = input()
        choice = self.parseText(selection)
        if choice =='u':
            self.useItem(self.hand)
            self.remove(self.hand)
        if choice == 'a':
            self.backpack.append(self.hand)
            self.hand = ''
        if choice == 's':
            print('backpack:' + str(self.backpack)[1:-1])
            print('Select an item to switch')
            selection = input()
            self.getFromBackpack(self.parseText(selection))
        elif choice == 'r':
            print('hand:' + self.hand)
            print('backpack:' + str(self.backpack)[1:-1])
            print('Select an item to remove')
            selection = input()
            self.remove(selection)

    def nextLevel(self):
        '''
        allows player to move onto next level
        '''
        self.stage.passed = True

newGame = game()
newGame.start()

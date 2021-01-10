
import random
import time

def displayIntro():
      print('''You are in a land full of dragons. In front of you,
  you see two caves. In one cave, the dragon is friendly
  and will share his treasure with you. The other dragon
  is greedy and hungry, and will eat you on sight.''')
      print()

def chooseCave():
     cave = ''
     while cave != '1' and cave != '2' and cave != '3':
         print('Which cave will you go into? (1, 2 or 3)')
         cave = input()
     return cave

def checkCave(chosenCave):
     print('You approach the cave...')
     time.sleep(2)
     print('It is dark and spooky...')
     time.sleep(2)
     print('A large dragon jumps out in front of you! He opens his jaws and...')
     time.sleep(2)
     mums_fukingCave = 1
     friendlyCave = 1
     print(f'friend{friendlyCave}')
     print(f'fuck {mums_fukingCave}')
     while mums_fukingCave == friendlyCave:
        mums_fukingCave = random.randint(1, 3)
        print(f'friend{friendlyCave}')
        print(f'fuck {mums_fukingCave}')

     if chosenCave == friendlyCave:
         print('Gives you his treasure!')
     elif chosenCave == mums_fukingCave:
        print('Fuck your mum!')
     else:
         print('Gobbles you down in one bite!')

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
     displayIntro()
     caveNumber = chooseCave()
     checkCave(caveNumber)

     print('Do you want to play again? (yes or no)')
     playAgain = input()
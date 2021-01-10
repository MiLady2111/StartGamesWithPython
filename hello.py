from random import randint
print('Hello! \nWhat is your name?')
name = input()
print('Hello ' + name + ', I\'m glad to see you!')



result = randint(0, 100)
print("Can you guess the number from 1 to 100?")
for count in range(15):
    player_num = int(input())
    if player_num < result:
        print("It's too small")
    elif player_num > result:
        print("It's too big")
    else:
        print("Congratulations, It's correct!")
        break
count = count +1
print("You can able guess to guess on " + str(count) + " attempts")
































































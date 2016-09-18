import os
import time
import sys
from random import randint


answer = 0
name = str()
tries = 0


try:
    os.system('say "{0}"'.format("Lets play a game!"))
    time.sleep(1)
    os.system('say "{0}"'.format("Whats your name?"))
    name = raw_input("Whats your name?: ")
    #print(str(name))
    os.system('say "{0}"'.format(name))
    time.sleep(1)

except:
    message = "broken"
    os.system('say "{0}"'.format(message + " " + "test"))
    time.sleep(1)

    sys.exit('operation completed')

for i in range(0,6):

    try:
        tries = tries + 1
        message = "I'm thinking of a number between 1 & 6"
        os.system('say "{0}"'.format(message))
        time.sleep(1)
        os.system('say "{0}"'.format("What is it?"))
        rando = randint(1,6)
        random = (str(rando))
        #print(random)
        answer = raw_input("Guess the number: ")
        print(answer)

    except:
        message = "broken"
        os.system('say "{0}"'.format(message + " " + "test"))
        time.sleep(1)

        sys.exit('operation completed')

    if (int(answer)) >= 7:
        message = "I said between 1 & 6!"
        os.system('say "{0}"'.format(message))
        time.sleep(1)
        os.system('say "{0}"'.format("You choose" + (str(answer))) + "are you stupid?")
        time.sleep(1)
        os.system('say "{0}"'.format("You wasted a turn, Try again"))

    elif answer == random:
        message = "You guessed correctly"
        os.system('say "{0}"'.format(message))
        time.sleep(1)
        os.system('say "{0}"'.format("I was thinking of" + (str(random))))
        time.sleep(1)
        os.system('say "{0}"'.format("Well done!"))


    else:
        message = "wrong"
        os.system('say "{0}"'.format(message))
        time.sleep(1)
        os.system('say "{0}"'.format("I was thinking of" + (str(random))))
        time.sleep(1)
        os.system('say "{0}"'.format("Lets try again! You have" + (str(6-(tries))) + "attempts left"))
# Name:
# Date:


""" 
proj 03: Guessing Game

Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, 
or exactly right. Keep the game going until the user types exit.
Keep track of how many guesses the user has taken, and when the game ends, print this out.

"""
import random
name = raw_input("What's your name?")
if name == "Abinav":
    na = int(raw_input("Guess a random number 1 through 9: "))
    if na == na:
        print "Congratulations! You got it first try!"
elif name == 'Chad':
    ni = int(raw_input("Guess a random number 1 through 9: "))
    if ni == 100000000000000002324235423542678:
        pass
    else:
        print "That's wrong. No more tries 'cause you're Chad."
else:
    user_input = int(raw_input("Guess a random number 1 through 9: "))
    var = random.randint(1, 9)
    if user_input == var:
        print "Congratulations! You got it first try!"
    else:
        print "That was wrong. You have two more tries."
        userinput2 = int(raw_input("Guess a random number 1 through 9: "))
        if userinput2 == var:
            print "Congratulations! You got it right!"
        else:
            print "That was wrong. You have one more try."
            user_input3 = int(raw_input("Guess a random number 1 through 9: "))
            if user_input3 == var:
                print "Third time's the charm, huh? Nice job!"
            else:
                print "The number was " + str(var)
                print "That was wrong. Try again and maybe you'll get lucky!"



#-----------------------------------------------------------------------------
# Name:        Kangaroo Kounter
# Purpose:     a fun game about counting kangaroos
# Author:      Iat Seng Kang
# Created:     14-Nov-2024
# Updated:     22-Nov-2024
#----------------------------------------------------------------------

#imports modules used in code
import random
import time
import os

#defines variables
high_score = {}
trial = []
run = 1
answer = "1"

#introduction, prints the rules of the game if you type "rules," then clears the system and begins the game
print("Welcome to The Kangaroo Kounter!")
rules = input('Please type "rules" to read the rules. Type anything else to start the game.\n')
if rules.lower() == "rules":
    print("The Kangaroo Kounter is pretty simple, it's about a game where you have to count the amount of kangaroos there are.")
    print("As you begin the game, the game will tell you how many baby kangaroos jumped into the mama's pouch.")
    print("After 5 seconds, you will need to tell me how many kangaroos there are. Don't forget to include the mama kangaroo!")
    print("If you guess the incorrect number, you will lose a life!")
    print("Don't worry too much though, you will start the game with 2 lives.")
    print("If you guess the correct number, you will earn a point and move onto the next round!")
    print("However, there will be one more wave of kangaroos to count this time.")
    print("I'm also feeling pretty generous, so each round you will be able to use a hint.")
    print('To use a hint, type "hint" when it asks you for the amount of kangaroos.')
    print("Then, input a number, and I'll tell you how many baby kangaroos had jumped in the pouch during that specific wave.")
    print("That's it! It's time to begin the game.")
    input("Type anything to continue.\n")
os.system('clear')

#while loop to initiate the game as long as user wants to keep playing
while answer == "1":

    #defines more variables that are reset each game
    lives = 2
    score = 0
    hint = False

    #runs game while you still have lives left
    while lives != 0:

        #defines more variables that are reset each round
        kangaroo_num = [1]
        total_kangaroos = 0

        #clears the console and prints what round it is, then pauses for 1.5 seconds
        os.system('clear')
        print(f"ROUND {score + 1}")
        time.sleep(1.5)

        #prints and stores your current "score" + 3 random random numbers then finds and stores the sum of all those numbers
        for i in range (score + 3):
            num = random.randint(1,9)
            print(f"{num} joey(s) jump into the mama's pouch")
            kangaroo_num.append(num)
        for i in kangaroo_num:
            total_kangaroos += i

        #waits for 5 seconds for the user to memorize the numbers then clears the console so the user can't cheat
        time.sleep(5)
        os.system('clear')

        #asks for user's guess
        guess = input("How many kangaroos are there?\n")

        #asks for wave number user would like to know about if "hint" is inputted and checks for validity. prints how many joeys there were in that wave
        while guess.lower() == "hint":
            if hint == False:
                wave_num = input("Which wave would you like to know about?\n")

                while len(wave_num) == 0:
                    print("Please enter a guess!")
                    wave_num = input("Which wave would you like to know about?\n")

                while not wave_num.isnumeric():
                    print("You must guess a whole number! Please fix this in your next guess")
                    wave_num = input("Which wave would you like to know about?\n")

                while int(wave_num) <= 0 or int(wave_num) > score + 3:
                    if int(wave_num) == 0:
                        print("Wave cannot be zero! Please fix this in your next guess")
                        wave_num = input("Which wave would you like to know about?\n")
                    elif int(wave_num) > score + 3:
                        print("That wave didn't happen! Please fix this is your next guess")
                        wave_num = input("Which wave would you like to know about?\n")
                    else:
                        print("You must guess a whole number! Please fix this in your next guess")
                        wave_num = input("Which wave would you like to know about?\n")

                print(f"During wave {wave_num}, {kangaroo_num[int(wave_num)]} joeys had jumped into the pouch")
                hint = True
                guess = input("how many kangaroos are there?\n")

            else:
                print("You have already used your hint this round!")
                guess = input("how many kangaroos are there?\n")

        #checks the input of the user's validity
        while len(guess) == 0:
            print("Please enter a guess!")
            guess = input("How many kangaroos are there?\n")

        while not guess.isnumeric():
            print("You must guess a whole number! Please fix this in your next guess")
            guess = input("How many kangaroos are there?\n")

        while int(guess) < 0:
            print("There cannot be a negative number of kangaroos silly! Please fix this in your next guess")
            guess = input("How many kangaroos are there?\n")

        #adds 1 to the score of the user if user's input is correct then loops previous code
        if int(guess) == total_kangaroos:
            print("Correct! There were a total of " + str(total_kangaroos) + " kangaroos!")
            score += 1

        #subtracts 1 from remaining lives if user's input is incorrect then tells user how many lives they have remaining
        else:
            lives -= 1
            print("Aw man! There were actually a total of " + str(total_kangaroos) + " kangaroos")
            print("You now have " + str(lives) + " lives left")

        #waits 1.5 seconds and then clears the console
        time.sleep(1.5)
        os.system('clear')

    #adds your run number and score to a dictionary
    kangaroo_num.pop(0)
    high_score.setdefault(run, score)

    #adds run number, round number, list of all the number of joeys, user's guess and actual amount to a list 
    trial.append(str(run))
    trial.append(score + 1)
    trial.append(kangaroo_num)
    trial.append(guess)
    trial.append(total_kangaroos)

    #adds one to the amount of games played
    run += 1


    #prints the end screen and score, and asks user whether they want to play again, see their score or see their high score
    print("GAME OVER")
    print("Score: " + str(score))
    answer = input("Type 1 if you would like to play again and try to beat your old score!\nType 2 if you want to see that last round of any previous game played\nType 3 if you want to see all your previous scores\nType 4 to see your current high score\nType anything else to exit the game\n")

    #asks for input based on what the user wants to do next. exits code if "1", "2", "3", or "4" are not inputted.
    while answer == "2" or answer == "3" or answer == "4":
        os.system('clear')

        #if "3" is inputted, prints all previous attempt scores
        if answer == "3":
            for key, value in high_score.items():
                print(f"Attempt {key} score: {value}\n")
            print("-" * 100)

            #asks for new input
            answer = input("Type 1 if you would like to play again and try to beat your old score!\nType 2 if you want to see that last round of any previous game played\nType 3 if you want to see all your previous scores\nType 4 to see your current high score\nType anything else to exit the game\n")

        #if "4" is inputted, prints the high score
        elif answer == "4":
            highest = 0
            for key, value in high_score.items():
                if value > highest:
                    highest = value
            print(f"Current high score: {highest}")
            print("Play again to try to beat your high score!")
            print("-" * 100)

            #asks for new input
            answer = input("Type 1 if you would like to play again and try to beat your old score!\nType 2 if you want to see that last round of any previous game played\nType 3 if you want to see all your previous scores\nType 4 to see your current high score\nType anything else to exit the game\n")

        #if "2" is inputted, asks user which attempt they would like to know about
        else:
            last = input("for which attempt would you like to see the last round you played?\n")

            #checks for validity
            while len(last) == 0:
                print("Please enter a attempt!")
                last = input("for which attempt would you like to see the last round you played?\n")

            while not last.isnumeric():
                print("Attempt must be a whole number! Please fix this in your next guess")
                last = input("for which attempt would you like to see the last round you played?\n")

            while int(last) <= 0 or int(last) > len(trial)/5:
                if int(last) == 0:
                    print("Attempt cannot be 0! Please fix this in your next guess")
                elif int(last) < 0:
                    print("Attempt must be a whole number! Please fix this in your next guess")
                else:
                    print("You haven't attempted that many times yet! Please fix this in your next guess")
                last = input("for which attempt would you like to see the last round you played?\n")

            #prints the attempt, round number, all the joeys that existed in that particular attempt and round, the user's guess and the actual amount
            for i in range(len(trial)):
                if trial[i] == last:
                    list_num = int(i)
            print(f"ATTEMPT {last}, ROUND {trial[list_num + 1]}\n")
            for i in trial[list_num + 2]:
                print(f"{i} joey(s) jump into the mama's pouch")
            print(f"\nYour guess: {trial[list_num + 3]}")
            print(f"Total amount: {trial[list_num + 4]}")
            print(f"Score: {trial[list_num + 1] - 1}")
            print("-" * 100)

            #asks for new input
            answer = input("Type 1 if you would like to play again and try to beat your old score!\nType 2 if you want to see that last round of any previous game played\nType 3 if you want to see all your previous scores\nType 4 to see your current high score\nType anything else to exit the game\n")



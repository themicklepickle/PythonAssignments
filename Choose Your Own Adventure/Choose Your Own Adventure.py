'''––––––––––––––––––––––––––––––––––––SET UP––––––––––––––––––––––––––––––––––––'''

'''MODULES'''

# random module for guessing games
import random

# time module for waiting effects
import time

'''FUNCTIONS'''


# choice
def options(numberOfOptions):
    # global variable
    global validInput
    global choice

    if numberOfOptions == 2:

        # variable for data sanitation
        validInput = False

        # inputs the player's choice
        choice = input("\nWhat should " + name + " do? (1/2): ")

        # data sanitation
        if choice == "1" or choice == "2":
            validInput = True

    elif numberOfOptions == 3:

        # variable for data sanitation
        validInput = False

        # inputs the player's choice
        choice = input("\nWhat should " + name + " do? (1/2/3): ")

        # data sanitation
        if choice == "1" or choice == "2" or choice == "3":
            validInput = True


# separator
def separator():
    # prints a horizontal line as a separator
    print("\n" + 140 * "–" + "\n")


# play the game again
def again():
    # global variable
    global validInput
    global tryAgain

    # variable for data sanitation
    validInput = False

    # inputs the player's choice
    choice = input("\nWhat should " + name + " do? (1/2): ")

    # data sanitation
    if choice == "1" or choice == "2":
        validInput = True

        if choice == "1":
            tryAgain = True
        else:
            tryAgain = False


# word guessing game
def wordGuessingGame():
    separator()

    print(name, "isn't the brightest star in the skies, but luckily the rules of this game are simple.")
    print("Simply choose a word and hopefully it matches what the computer has chosen.")
    print("If the word matches, then you win.")

    wordGuess = input("\nWhat is your guess?: ")

    print("\n" + name + "'s guess:", wordGuess)

    words = open("words.txt", "r").read().splitlines()
    wordAnswer = random.choice(words)
    print("Correct answer:", wordAnswer)

    separator()


# number guessing game
def numberGuessingGame():
    separator()

    print("Surprisingly, the name of this game is not misleading.")
    print("Simply choose a number and hopefully it matches what the computer has chosen.")
    print("If the number matches, then you win.")

    numberGuess = input("\nWhat is your guess?: ")

    print("\n" + name + "'s guess:", numberGuess)

    numberAnswer = random.randint(1, 10000000)
    print("Correct answer:", numberAnswer)

    separator()


# end
def end():
    separator()

    print("THE END")


# play again
def playAgain():
    # global variable
    global validInput
    global playAgainResult

    # variable for data sanitation
    validInput = False

    separator()

    playAgainInput = input("Do you want to play again? Yes (1) or No (2): ")

    # data sanitation
    if playAgainInput == "1" or playAgainInput == "2":
        validInput = True

        separator()

        if playAgainInput == "1":
            playAgainResult = True

        else:
            playAgainResult = False


'''PLAY AGAIN SETUP'''

playAgainResult = True

'''––––––––––––––––––––––––––––––––––GAME STARTS––––––––––––––––––––––––––––––––––'''

while playAgainResult == True:

    # greeting and asks the user for their name
    print("Welcome to Michael's choose your own adventure game!\n")
    name = input("Choose a name for yourself: ")

    # calls separator function
    separator()

    # displays the initial situation that the user is in
    print("After a long day of school,", name, "finds themself bored in their room.")
    print(name, "reaches for their laptop and boots it up.")
    print("After hearing the nostalgic start up sound,", name, "is prompted with 3 choices.")

    # provides the set of choices (python/folder/chrome)
    print("\n" + name, "can open a python module (1), open a folder (2) or open google chrome (3)")

    # calls options function
    options(3)

    # data sanitation
    while validInput == False:
        print("INVALID CHOICE")
        options(3)

    # calls separator function
    separator()

    # open a python module
    if choice == "1":
        print("opening untitled project", end="")
        time.sleep(1)
        print(".", end="")
        time.sleep(1)
        print(".", end="")
        time.sleep(1)
        print(".")
        time.sleep(1)

        print("\nWelcome to the world's first python game!")

        # provides the set of choices (word guessing game/number guessing game/unlisted option)
        print("\n" + name, "can play a word guessing game (1) or number guessing game (2)")

        # calls choice function
        options(2)

        # data sanitation
        while validInput == False:
            print("INVALID CHOICE")
            options(2)

        # word guessing game
        if choice == "1":
            tryAgain = True
            while tryAgain == True:

                # game
                wordGuessingGame()

                # lost the game
                print(name + " has lost the game.", name + " can try again (1) or quit (2)")

                # asks the user if they want to play again
                again()

                # data sanitation
                while validInput == False:
                    print("INVALID CHOICE")
                    again()

            separator()

            # asks user if they are done with the computer
            print(name, "can either be done with the computer (1) or continue to use it (2)")

            # calls options function
            options(2)

            # data sanitation
            while validInput == False:
                print("INVALID CHOICE")
                options(2)

            # done with computer
            if choice == "1":

                separator()

                print(name, "is enraged by their sub-human guessing skills.")
                print(name, "casually removes the pitchfork hanging above their bed.")
                print("With all their might,", name, "thrusts the pitchfork through the computer.")

                end()

                playAgain()

                # data sanitation
                while validInput == False:
                    print("INVALID CHOICE")
                    playAgain()

            else:

                separator()

                print("Continue to use it?", end="")
                time.sleep(1)
                print("?", end="")
                time.sleep(1)
                print("?")
                time.sleep(1)
                print(".", end="")
                time.sleep(1)
                print(".", end="")
                time.sleep(1)
                print(".")
                time.sleep(1)
                print("You wish! The computer is fed up with", name + "'s subhuman guessing skills!")
                time.sleep(2)
                print("\nGoodbye.")
                time.sleep(1)
                print("\nInitiating self destruct sequence", end="")
                time.sleep(1)
                print(".", end="")
                time.sleep(1)
                print(".", end="")
                time.sleep(1)
                print(".")

                print("\nBOOM!!!")

                end()

                playAgain()

                # data sanitation
                while validInput == False:
                    print("INVALID CHOICE")
                    playAgain()

        # number guessing game
        elif choice == "2":
            tryAgain = True
            while tryAgain == True:

                # game
                numberGuessingGame()

                # lost the game
                print(name + " has lost the game.", name + " can try again (1) or quit (2)")

                # asks the user if they want to play again
                again()

                # data sanitation
                while validInput == False:
                    print("INVALID CHOICE")
                    again()

            separator()

            # asks user if they are done with the computer
            print(name, "can either be done with the computer (1) or continue to use it (2)")

            # calls options function
            options(2)

            # data sanitation
            while validInput == False:
                print("INVALID CHOICE")
                options(2)

            # done with computer
            if choice == "1":

                separator()

                print(name, "is enraged by their sub-human guessing skills.")
                print(name, "casually removes the pitchfork hanging above their bed.")
                print("With all their might,", name, "thrusts the pitchfork through the computer.")

                end()

                playAgain()

                # data sanitation
                while validInput == False:
                    print("INVALID CHOICE")
                    playAgain()

            else:

                separator()

                print("Continue to use it?", end="")
                time.sleep(1)
                print("?", end="")
                time.sleep(1)
                print("?")
                time.sleep(1)
                print(".", end="")
                time.sleep(1)
                print(".", end="")
                time.sleep(1)
                print(".")
                time.sleep(1)
                print("You wish! The computer is fed up with", name + "'s subhuman guessing skills!")
                time.sleep(2)
                print("\nGoodbye.")
                time.sleep(1)
                print("\nInitiating self destruct sequence", end="")
                time.sleep(1)
                print(".", end="")
                time.sleep(1)
                print(".", end="")
                time.sleep(1)
                print(".")

                print("\nBOOM!!!")

                end()

                playAgain()

                # data sanitation
                while validInput == False:
                    print("INVALID CHOICE")
                    playAgain()

        # unlisted option
        else:
            print("YOU HAVE BROKEN THE GAME!!!")

    # open a folder
    elif choice == "2":
        print("opening folder", end="")
        time.sleep(1)
        print(".", end="")
        time.sleep(1)
        print(".", end="")
        time.sleep(1)
        print(".")
        time.sleep(1)

        print("\n" + name, "is presented with three file types to access.")

        # provides first set of choices (image/word doc/video)
        print("\n" + name, "can open an image (1) or a video (2) or a python module (3)")

        # calls option function
        options(3)

        # data sanitation
        while validInput == False:
            print("INVALID CHOICE")
            options(3)

            # image
        if choice == "1":

            separator()

            print("The image turns out to be a meme about TRUMP.")
            print("In fact, its the funniest meme that", name, "has ever seen.")
            print(name, "bursts out laughing.")

            print('\n"HAHAHAHAHAHAHAHA"')

            print("\nAfter a while,", name, "regains control of their funny bone.")

            print("\n" + name, "can send the meme to a friend (1) or set it as their background (2)")

            # calls option function
            options(2)

            # data sanitation
            while validInput == False:
                print("INVALID CHOICE")
                options(2)

                # send the meme to a friend
            if choice == "1":

                separator()

                print("\nIt turns out that the meme is also the funniest that", name + "'s friend has ever seen.")

                print("\n" + name, "spends the entire night chatting with their friend.")
                print(
                    "Their conversation jumps from politics to their favourite songs to how ready they are for winter break.")
                print("Naturally,", name,
                      "loses track of time and at 2 am (aka crackhead hours) they begin to doze off.")
                print(name, "has laughed more in this one night than their entire life.")

                print("\n...")

                print("\nHaving used up all of their energy,", name, "sleeps through the next day")
                print("...and the day after that")
                print("...and the day after that.")

                print("\nThat would be the last of", name + ".")
                print("The laughter inflicted by the meme was too much for", name + "'s body to handle.")

                print("\nHowever, the ramifications weren't contained to", name + ".")
                print(name + "'s friend would end up sharing the meme with even more friends.")
                print("In a chain reaction, the entire world was laughing...at a meme about TRUMP.")
                print("With the wave of laughter came a wave of eternal sleep.")

                print(
                    "\nNot climate change, not war, but a single meme was responsible for the extinction of the human race.")

                end()

                playAgain()

                # data sanitation
                while validInput == False:
                    print("INVALID CHOICE")
                    playAgain()

            # set it as their background
            else:

                separator()

                print("Plagued by the humor of the meme,", name, "starts to laugh uncontrollably again.")

                print("\n" + name, "feels immensely compelled to share their happiness with others.")
                print(name, "whips out their phone and sends it to their closest friend.")

                print("\nIt turns out that the meme is also the funniest that", name + "'s friend has ever seen.")

                print("\n" + name, "spends the entire night chatting with their friend.")
                print(
                    "Their conversation jumps from politics to their favourite songs to how ready they are for winter break.")
                print("Naturally,", name,
                      "loses track of time and at 2 am (aka crackhead hours) they begin to doze off.")
                print(name, "has laughed more in this one night than their entire life.")

                print("\n...")

                print("\nHaving used up all of their energy,", name, "sleeps through the next day")
                print("...and the day after that")
                print("...and the day after that.")

                print("\nThat would be the last of", name + ".")
                print("The laughter inflicted by the meme was too much for", name + "'s body to handle.")

                print("\nHowever, the ramifications weren't contained to", name + ".")
                print(name + "'s friend would end up sharing the meme with even more friends.")
                print("In a chain reaction, the entire world was laughing...at a meme about TRUMP.")
                print("With the wave of laughter came a wave of eternal sleep.")

                print(
                    "\nNot climate change, not war, but a single meme was responsible for the extinction of the human race.")

                end()

                playAgain()

                # data sanitation
                while validInput == False:
                    print("INVALID CHOICE")
                    playAgain()

        # video
        elif choice == "2":

            separator()

            print("buffering untitled video", end="")
            time.sleep(1)
            print(".", end="")
            time.sleep(1)
            print(".", end="")
            time.sleep(1)
            print(".")
            time.sleep(1)

            print("\nAn intriguing video of a Minecraft Lets Play is displayed.")
            print("Satisfied with the quality of the video,", name, "goes on Youtube to watch another.")

            print("\n" + name, "arrives on the Youtube homepage.")
            print("Of the various recommended videos, one in particular catches their attention.")
            print('The video is titled "NUCLEAR LAUNCH CODES"')

            print("\nAware of the issue of clickbait,", name, "is initially skeptical.")

            print("\n" + name, "can watch the video (1) or watch another video (2)")

            # calls option function
            options(2)

            # data sanitation
            while validInput == False:
                print("INVALID CHOICE")
                options(2)

            # watch the video
            if choice == "1":

                separator()

                print(name, "clicks on the thumbnail and begins to watch the video.")

                print(".", end="")
                time.sleep(1)
                print(".", end="")
                time.sleep(1)
                print(".")
                time.sleep(1)

                print(
                    "Midway through, the video explains that the viewer must subscribe immediately to get the nuclear codes.")

                print("\n" + name, "can either subscribe (1) or continue watching (2)")

                # calls option function
                options(2)

                # data sanitation
                while validInput == False:
                    print("INVALID CHOICE")
                    options(2)

                # subscribe
                if choice == "1":

                    separator()

                    print("DING!")

                    print("\n" + name, "appears to have recieved an email.")
                    print(name,
                          'opens their email and sure enough, they have an unread email with the subject, "NUCLEAR CODES"')

                    print("\n" + name, "can attempt to dominate the world (1) or keep the codes discreet (2)")

                    # calls option function
                    options(2)

                    # data sanitation
                    while validInput == False:
                        print("INVALID CHOICE")
                        options(2)

                    # attempt to dominate the world
                    if choice == "1":

                        separator()

                        print(name, "takes a road trip to 1600 Pennsylvania Ave, The White House.")

                        print("\n" + name, "informs TRUMP of his knowledge of the nuclear codes.")
                        print(name, "is instantaneously named president of the United States.")

                        print("\nA couple hours later, global leaders come together to discuss how to handle", name)
                        print("They decide that", name, "should have absolute power over the world.")

                        print("\n" + name, "decides to unify every country in the world and call it", name + "land.")

                        print("\nUnder the leadership of", name, "all crime and hate within the world vanishes.")

                        print("\nEssentially,", name, "went from being a bored kid to the supreme ruler of",
                              name + "land.")

                        print("\nA pretty good day...")

                        print("\n:)")

                        end()

                        playAgain()

                        # data sanitation
                        while validInput == False:
                            print("INVALID CHOICE")
                            playAgain()

                    # keep the codes discreet
                    else:

                        separator()

                        print(name, "decides to close the email tab and continues on with their day.")

                        separator()

                        print("The next day,", name, "hears banging on their front door.")
                        print('The banging subsides, but is replaced by a startling "FBI OPEN UP"')
                        print("With no intention to disobey the FBI,", name, "promptly opens the door.")

                        print("\n" + name, "is forcefully handcuffed and forced into the back of a black SUV.")

                        print("\nThe FBI had found out that", name, "has access to the nuclear codes.")
                        print(name,
                              "is charged as a threat to global security and is sentenced to life in prison at The Hague.")

                        print("\nA pretty bad day...")

                        print("\n:(")

                        end()

                        playAgain()

                        # data sanitation
                        while validInput == False:
                            print("INVALID CHOICE")
                            playAgain()


                # continue watching
                else:

                    separator()

                    print(name, "ignores the instructions of the video and continues watching the video.")
                    print("Towards the end of the video, a link appears.")

                    print("\nTo resolve their insatiable curiosity,", name, "clicks on the link.")
                    print("A tab opens and a single image is displayed.")

                    print("\n" + name, "is directed to a meme about TRUMP.")
                    print("In fact, its the funniest meme that", name, "has ever seen.")
                    print(name, "bursts out laughing.")

                    print('\n"HAHAHAHAHAHAHAHA"')

                    print("\nAfter a while,", name, "regains control of their funny bone.")

                    print("\n" + name, "can send the meme to a friend (1) or set it as their background (2)")

                    # calls option function
                    options(2)

                    # data sanitation
                    while validInput == False:
                        print("INVALID CHOICE")
                        options(2)

                        # send the meme to a friend
                    if choice == "1":

                        separator()

                        print("\nIt turns out that the meme is also the funniest that",
                              name + "'s friend has ever seen.")

                        print("\n" + name, "spends the entire night chatting with their friend.")
                        print(
                            "Their conversation jumps from politics to their favourite songs to how ready they are for winter break.")
                        print("Naturally,", name,
                              "loses track of time and at 2 am (aka crackhead hours) they begin to doze off.")
                        print(name, "has laughed more in this one night than their entire life.")

                        print("\n...")

                        print("\nHaving used up all of their energy,", name, "sleeps through the next day")
                        print("...and the day after that")
                        print("...and the day after that.")

                        print("\nThat would be the last of", name + ".")
                        print("The laughter inflicted by the meme was too much for", name + "'s body to handle.")

                        print("\nHowever, the ramifications weren't contained to", name + ".")
                        print(name + "'s friend would end up sharing the meme with even more friends.")
                        print("In a chain reaction, the entire world was laughing...at a meme about TRUMP.")
                        print("With the wave of laughter came a wave of eternal sleep.")

                        print(
                            "\nNot climate change, not war, but a single meme was responsible for the extinction of the human race.")

                        end()

                        playAgain()

                        # data sanitation
                        while validInput == False:
                            print("INVALID CHOICE")
                            playAgain()

                    # set it as their background
                    else:

                        separator()

                        print("Plagued by the humor of the meme,", name, "starts to laugh uncontrollably again.")

                        print("\n" + name, "feels immensely compelled to share their happiness with others.")
                        print(name, "whips out their phone and sends it to their closest friend.")

                        print("\nIt turns out that the meme is also the funniest that",
                              name + "'s friend has ever seen.")

                        print("\n" + name, "spends the entire night chatting with their friend.")
                        print(
                            "Their conversation jumps from politics to their favourite songs to how ready they are for winter break.")
                        print("Naturally,", name,
                              "loses track of time and at 2 am (aka crackhead hours) they begin to doze off.")
                        print(name, "has laughed more in this one night than their entire life.")

                        print("\n...")

                        print("\nHaving used up all of their energy,", name, "sleeps through the next day")
                        print("...and the day after that")
                        print("...and the day after that.")

                        print("\nThat would be the last of", name + ".")
                        print("The laughter inflicted by the meme was too much for", name + "'s body to handle.")

                        print("\nHowever, the ramifications weren't contained to", name + ".")
                        print(name + "'s friend would end up sharing the meme with even more friends.")
                        print("In a chain reaction, the entire world was laughing...at a meme about TRUMP.")
                        print("With the wave of laughter came a wave of eternal sleep.")

                        print(
                            "\nNot climate change, not war, but a single meme was responsible for the extinction of the human race.")

                        end()

                        playAgain()

                        # data sanitation
                        while validInput == False:
                            print("INVALID CHOICE")
                            playAgain()

            # watch another video
            else:

                separator()

                print(name, "continues to browse Youtube.")

                print("\nAfter wasting away several hours of their life watching Youtube,", name,
                      "decides to become a Youtuber themself.")
                print("By building a target audience primarily consisting of gullible 12 year olds,", name,
                      "rapidly climbs the ranks.")

                print("\nOne day,", name, "is approached by Mr. Beast and a plethora of their Youtube idols.")
                print("They wanted", name, 'to join their initiative coined "Team Trees."')

                print("\n" + name, "gladly accepts the offer.")

                print("\nTwo months later, Team Trees has successfully raised $20 million dollars, primarily thanks to",
                      name + ".")

                print("\nThrilled by their success, Youtube approaches", name,
                      "and offers them an irresistable job opportunity.")
                print("With this career,", name,
                      "would not only earn a hefty paycheck, but also have access to all of Youtube's data.")

                print("A few years into their career,", name, "is offered a deal by TRUMP.")
                print("In order to get re-elected, TRUMP wants to investigate his political rivals and", name,
                      "can get him that information.")

                print("\n" + name, "can either share Youtube's data (1) or stay out of TRUMP's blatent collusion (2)")

                # calls option function
                options(2)

                # data sanitation
                while validInput == False:
                    print("INVALID CHOICE")
                    options(2)

                # share Youtube's data
                if choice == "1":

                    separator()

                    print(name, "decides to share Youtube's data with TRUMP.")

                    print("The next day,", name, "hears banging on their front door.")
                    print('The banging subsides, but is replaced by a startling "FBI OPEN UP!"')
                    print("With no intention to disobey the FBI,", name, "promptly opens the door.")

                    print("\n" + name, "is forcefully handcuffed and forced into the back of a black SUV.")

                    print("\nThe FBI had found out that", name, "had helped TRUMP collude.")
                    print(name, "is charged with obstruction of justice and is sentenced to life in prison.")

                    print("\nA pretty bad life...")

                    print("\n:(")

                    end()

                    playAgain()

                    # data sanitation
                    while validInput == False:
                        print("INVALID CHOICE")
                        playAgain()

                # stay out of TRUMP's blatent collusion
                else:

                    separator()

                    print(name, "decides to ignore TRUMP's requests.")

                    print("\nFurious, TRUMP lashes out on twitter about",
                          name + ", leaving out the collusion part, of course.")

                    print("\nMoments later,", name,
                          "receives a call from Youtube informing them that they have been fired.")

                    print("\n" + name, "lives out a pretty decent, average life.")
                    print("Although", name,
                          "didn't do much in their life time...at least they planted 20 million trees!")

                    end()

                    playAgain()

                    # data sanitation
                    while validInput == False:
                        print("INVALID CHOICE")
                        playAgain()

        # python module
        else:

            print("opening untitled project", end="")
            time.sleep(1)
            print(".", end="")
            time.sleep(1)
            print(".", end="")
            time.sleep(1)
            print(".")
            time.sleep(1)

            print("\nWelcome to the world's first python game!")

            # provides the set of choices (word guessing game/number guessing game/unlisted option)
            print("\n" + name, "can play a word guessing game (1) or number guessing game (2)")

            # calls choice function
            options(2)

            # data sanitation
            while validInput == False:
                print("INVALID CHOICE")
                options(2)

            # word guessing game
            if choice == "1":
                tryAgain = True
                while tryAgain == True:

                    # game
                    wordGuessingGame()

                    # lost the game
                    print(name + " has lost the game.", name + " can try again (1) or quit (2)")

                    # asks the user if they want to play again
                    again()

                    # data sanitation
                    while validInput == False:
                        print("INVALID CHOICE")
                        again()

                separator()

                # asks user if they are done with the computer
                print(name, "can either be done with the computer (1) or continue to use it (2)")

                # calls options function
                options(2)

                # data sanitation
                while validInput == False:
                    print("INVALID CHOICE")
                    options(2)

                # done with computer
                if choice == "1":

                    separator()

                    print(name, "is enraged by their sub-human guessing skills.")
                    print(name, "casually removes the pitchfork hanging above their bed.")
                    print("With all their might,", name, "thrusts the pitchfork through the computer.")

                    end()

                    playAgain()

                    # data sanitation
                    while validInput == False:
                        print("INVALID CHOICE")
                        playAgain()

                else:

                    separator()

                    print("Continue to use it?", end="")
                    time.sleep(1)
                    print("?", end="")
                    time.sleep(1)
                    print("?")
                    time.sleep(1)
                    print(".", end="")
                    time.sleep(1)
                    print(".", end="")
                    time.sleep(1)
                    print(".")
                    time.sleep(1)
                    print("You wish! The computer is fed up with", name + "'s subhuman guessing skills!")
                    time.sleep(2)
                    print("\nGoodbye.")
                    time.sleep(1)
                    print("\nInitiating self destruct sequence", end="")
                    time.sleep(1)
                    print(".", end="")
                    time.sleep(1)
                    print(".", end="")
                    time.sleep(1)
                    print(".")

                    print("\nBOOM!!!")

                    end()

                    playAgain()

                    # data sanitation
                    while validInput == False:
                        print("INVALID CHOICE")
                        playAgain()

            # number guessing game
            elif choice == "2":
                tryAgain = True
                while tryAgain == True:

                    # game
                    numberGuessingGame()

                    # lost the game
                    print(name + " has lost the game.", name + " can try again (1) or quit (2)")

                    # asks the user if they want to play again
                    again()

                    # data sanitation
                    while validInput == False:
                        print("INVALID CHOICE")
                        again()

                separator()

                # asks user if they are done with the computer
                print(name, "can either be done with the computer (1) or continue to use it (2)")

                # calls options function
                options(2)

                # data sanitation
                while validInput == False:
                    print("INVALID CHOICE")
                    options(2)

                # done with computer
                if choice == "1":

                    separator()

                    print(name, "is enraged by their sub-human guessing skills.")
                    print(name, "casually removes the pitchfork hanging above their bed.")
                    print("With all their might,", name, "thrusts the pitchfork through the computer.")

                    end()

                    playAgain()

                    # data sanitation
                    while validInput == False:
                        print("INVALID CHOICE")
                        playAgain()

                else:

                    separator()

                    print("Continue to use it?", end="")
                    time.sleep(1)
                    print("?", end="")
                    time.sleep(1)
                    print("?")
                    time.sleep(1)
                    print(".", end="")
                    time.sleep(1)
                    print(".", end="")
                    time.sleep(1)
                    print(".")
                    time.sleep(1)
                    print("You wish! The computer is fed up with", name + "'s subhuman guessing skills!")
                    time.sleep(2)
                    print("\nGoodbye.")
                    time.sleep(1)
                    print("\nInitiating self destruct sequence", end="")
                    time.sleep(1)
                    print(".", end="")
                    time.sleep(1)
                    print(".", end="")
                    time.sleep(1)
                    print(".")

                    print("\nBOOM!!!")

                    end()

                    playAgain()

                    # data sanitation
                    while validInput == False:
                        print("INVALID CHOICE")
                        playAgain()

            # unlisted option
            else:
                print("YOU HAVE BROKEN THE GAME!!!")

    # open google chrome
    else:
        print("opening chrome", end="")
        time.sleep(1)
        print(".", end="")
        time.sleep(1)
        print(".", end="")
        time.sleep(1)
        print(".")
        time.sleep(1)

        print("\n" + name, "can do three things on google chrome.")

        # provides first set of choices (coolmathgames/Youtube/I'm feeling lucky)
        print("\n" + name, "can visit coolmathgames (1) or Youtube (2) or I'm feeling lucky (3)")

        # calls option function
        options(3)

        # data sanitation
        while validInput == False:
            print("INVALID CHOICE")
            options(3)

        # coolmathgames
        if choice == "1":

            separator()

            # provides the set of choices (word guessing game/number guessing game/unlisted option)
            print("\n" + name, "can play a word guessing game (1) or number guessing game (2)")

            # calls choice function
            options(2)

            # data sanitation
            while validInput == False:
                print("INVALID CHOICE")
                options(2)

            # word guessing game
            if choice == "1":
                tryAgain = True
                while tryAgain == True:

                    # game
                    wordGuessingGame()

                    # lost the game
                    print(name + " has lost the game.", name + " can try again (1) or quit (2)")

                    # asks the user if they want to play again
                    again()

                    # data sanitation
                    while validInput == False:
                        print("INVALID CHOICE")
                        again()

                separator()

                # asks user if they are done with the computer
                print(name, "can either be done with the computer (1) or continue to use it (2)")

                # calls options function
                options(2)

                # data sanitation
                while validInput == False:
                    print("INVALID CHOICE")
                    options(2)

                # done with computer
                if choice == "1":

                    separator()

                    print(name, "is enraged by their sub-human guessing skills.")
                    print(name, "casually removes the pitchfork hanging above their bed.")
                    print("With all their might,", name, "thrusts the pitchfork through the computer.")

                    end()

                    playAgain()

                    # data sanitation
                    while validInput == False:
                        print("INVALID CHOICE")
                        playAgain()

                else:

                    separator()

                    print("Continue to use it?", end="")
                    time.sleep(1)
                    print("?", end="")
                    time.sleep(1)
                    print("?")
                    time.sleep(1)
                    print(".", end="")
                    time.sleep(1)
                    print(".", end="")
                    time.sleep(1)
                    print(".")
                    time.sleep(1)
                    print("You wish! The computer is fed up with", name + "'s subhuman guessing skills!")
                    time.sleep(2)
                    print("\nGoodbye.")
                    time.sleep(1)
                    print("\nInitiating self destruct sequence", end="")
                    time.sleep(1)
                    print(".", end="")
                    time.sleep(1)
                    print(".", end="")
                    time.sleep(1)
                    print(".")

                    print("\nBOOM!!!")

                    end()

                    playAgain()

                    # data sanitation
                    while validInput == False:
                        print("INVALID CHOICE")
                        playAgain()

            # number guessing game
            elif choice == "2":
                tryAgain = True
                while tryAgain == True:

                    # game
                    numberGuessingGame()

                    # lost the game
                    print(name + " has lost the game.", name + " can try again (1) or quit (2)")

                    # asks the user if they want to play again
                    again()

                    # data sanitation
                    while validInput == False:
                        print("INVALID CHOICE")
                        again()

                separator()

                # asks user if they are done with the computer
                print(name, "can either be done with the computer (1) or continue to use it (2)")

                # calls options function
                options(2)

                # data sanitation
                while validInput == False:
                    print("INVALID CHOICE")
                    options(2)

                # done with computer
                if choice == "1":

                    separator()

                    print(name, "is enraged by their sub-human guessing skills.")
                    print(name, "casually removes the pitchfork hanging above their bed.")
                    print("With all their might,", name, "thrusts the pitchfork through the computer.")

                    end()

                    playAgain()

                    # data sanitation
                    while validInput == False:
                        print("INVALID CHOICE")
                        playAgain()

                else:

                    separator()

                    print("Continue to use it?", end="")
                    time.sleep(1)
                    print("?", end="")
                    time.sleep(1)
                    print("?")
                    time.sleep(1)
                    print(".", end="")
                    time.sleep(1)
                    print(".", end="")
                    time.sleep(1)
                    print(".")
                    time.sleep(1)
                    print("You wish! The computer is fed up with", name + "'s subhuman guessing skills!")
                    time.sleep(2)
                    print("\nGoodbye.")
                    time.sleep(1)
                    print("\nInitiating self destruct sequence", end="")
                    time.sleep(1)
                    print(".", end="")
                    time.sleep(1)
                    print(".", end="")
                    time.sleep(1)
                    print(".")

                    print("\nBOOM!!!")

                    end()

                    playAgain()

                    # data sanitation
                    while validInput == False:
                        print("INVALID CHOICE")
                        playAgain()

            # unlisted option
            else:
                print("YOU HAVE BROKEN THE GAME!!!")

        # Youtube
        elif choice == "2":

            separator()

            print(name, "arrives on the Youtube homepage.")
            print("Of the various recommended videos, one in particular catches their attention.")
            print('The video is titled "NUCLEAR LAUNCH CODES"')

            print("\nAware of the issue of clickbait,", name, "is initially skeptical.")

            print("\n" + name, "can watch the video (1) or watch another video (2)")

            # calls option function
            options(2)

            # data sanitation
            while validInput == False:
                print("INVALID CHOICE")
                options(2)

            # watch the video
            if choice == "1":

                separator()

                print(name, "clicks on the thumbnail and begins to watch the video.")

                print(".", end="")
                time.sleep(1)
                print(".", end="")
                time.sleep(1)
                print(".")
                time.sleep(1)

                print(
                    "Midway through, the video explains that the viewer must subscribe immediately to get the nuclear codes.")

                print("\n" + name, "can either subscribe (1) or continue watching (2)")

                # calls option function
                options(2)

                # data sanitation
                while validInput == False:
                    print("INVALID CHOICE")
                    options(2)

                # subscribe
                if choice == "1":

                    separator()

                    print("DING!")

                    print("\n" + name, "appears to have recieved an email.")
                    print(name,
                          'opens their email and sure enough, they have an unread email with the subject, "NUCLEAR CODES"')

                    print("\n" + name, "can attempt to dominate the world (1) or keep the codes discreet (2)")

                    # calls option function
                    options(2)

                    # data sanitation
                    while validInput == False:
                        print("INVALID CHOICE")
                        options(2)

                    # attempt to dominate the world
                    if choice == "1":

                        separator()

                        print(name, "takes a road trip to 1600 Pennsylvania Ave, The White House.")

                        print("\n" + name, "informs TRUMP of his knowledge of the nuclear codes.")
                        print(name, "is instantaneously named president of the United States.")

                        print("\nA couple hours later, global leaders come together to discuss how to handle", name)
                        print("They decide that", name, "should have absolute power over the world.")

                        print("\n" + name, "decides to unify every country in the world and call it", name + "land.")

                        print("\nUnder the leadership of", name, "all crime and hate within the world vanishes.")

                        print("\nEssentially,", name, "went from being a bored kid to the supreme ruler of",
                              name + "land.")

                        print("\nA pretty good day...")

                        print("\n:)")

                        end()

                        playAgain()

                        # data sanitation
                        while validInput == False:
                            print("INVALID CHOICE")
                            playAgain()

                    # keep the codes discreet
                    else:

                        separator()

                        print(name, "decides to close the email tab and continues on with their day.")

                        separator()

                        print("The next day,", name, "hears banging on their front door.")
                        print('The banging subsides, but is replaced by a startling "FBI OPEN UP"')
                        print("With no intention to disobey the FBI,", name, "promptly opens the door.")

                        print("\n" + name, "is forcefully handcuffed and forced into the back of a black SUV.")

                        print("\nThe FBI had found out that", name, "has access to the nuclear codes.")
                        print(name,
                              "is charged as a threat to global security and is sentenced to life in prison at The Hague.")

                        print("\nA pretty bad day...")

                        print("\n:(")

                        end()

                        playAgain()

                        # data sanitation
                        while validInput == False:
                            print("INVALID CHOICE")
                            playAgain()


                # continue watching
                else:

                    separator()

                    print(name, "ignores the instructions of the video and continues watching the video.")
                    print("Towards the end of the video, a link appears.")

                    print("\nTo resolve their insatiable curiosity,", name, "clicks on the link.")
                    print("A tab opens and a single image is displayed.")

                    print("\n" + name, "is directed to a meme about TRUMP.")
                    print("In fact, its the funniest meme that", name, "has ever seen.")
                    print(name, "bursts out laughing.")

                    print('\n"HAHAHAHAHAHAHAHA"')

                    print("\nAfter a while,", name, "regains control of their funny bone.")

                    print("\n" + name, "can send the meme to a friend (1) or set it as their background (2)")

                    # calls option function
                    options(2)

                    # data sanitation
                    while validInput == False:
                        print("INVALID CHOICE")
                        options(2)

                        # send the meme to a friend
                    if choice == "1":

                        separator()

                        print("It turns out that the meme is also the funniest that", name + "'s friend has ever seen.")

                        print("\n" + name, "spends the entire night chatting with their friend.")
                        print(
                            "Their conversation jumps from politics to their favourite songs to how ready they are for winter break.")
                        print("Naturally,", name,
                              "loses track of time and at 2 am (aka crackhead hours) they begin to doze off.")
                        print(name, "has laughed more in this one night than their entire life.")

                        print("\n...")

                        print("\nHaving used up all of their energy,", name, "sleeps through the next day")
                        print("...and the day after that")
                        print("...and the day after that.")

                        print("\nThat would be the last of", name + ".")
                        print("The laughter inflicted by the meme was too much for", name + "'s body to handle.")

                        print("\nHowever, the ramifications weren't contained to", name + ".")
                        print(name + "'s friend would end up sharing the meme with even more friends.")
                        print("In a chain reaction, the entire world was laughing...at a meme about TRUMP.")
                        print("With the wave of laughter came a wave of eternal sleep.")

                        print(
                            "\nNot climate change, not war, but a single meme was responsible for the extinction of the human race.")

                        end()

                        playAgain()

                        # data sanitation
                        while validInput == False:
                            print("INVALID CHOICE")
                            playAgain()

                    # set it as their background
                    else:

                        separator()

                        print("Plagued by the humor of the meme,", name, "starts to laugh uncontrollably again.")

                        print("\n" + name, "feels immensely compelled to share their happiness with others.")
                        print(name, "whips out their phone and sends it to their closest friend.")

                        print("\nIt turns out that the meme is also the funniest that",
                              name + "'s friend has ever seen.")

                        print("\n" + name, "spends the entire night chatting with their friend.")
                        print(
                            "Their conversation jumps from politics to their favourite songs to how ready they are for winter break.")
                        print("Naturally,", name,
                              "loses track of time and at 2 am (aka crackhead hours) they begin to doze off.")
                        print(name, "has laughed more in this one night than their entire life.")

                        print("\n...")

                        print("\nHaving used up all of their energy,", name, "sleeps through the next day")
                        print("...and the day after that")
                        print("...and the day after that.")

                        print("\nThat would be the last of", name + ".")
                        print("The laughter inflicted by the meme was too much for", name + "'s body to handle.")

                        print("\nHowever, the ramifications weren't contained to", name + ".")
                        print(name + "'s friend would end up sharing the meme with even more friends.")
                        print("In a chain reaction, the entire world was laughing...at a meme about TRUMP.")
                        print("With the wave of laughter came a wave of eternal sleep.")

                        print(
                            "\nNot climate change, not war, but a single meme was responsible for the extinction of the human race.")

                        end()

                        playAgain()

                        # data sanitation
                        while validInput == False:
                            print("INVALID CHOICE")
                            playAgain()

            # watch another video
            else:

                separator()

                print(name, "continues to browse Youtube.")

                print("\nAfter wasting away several hours of their life watching Youtube,", name,
                      "decides to become a Youtuber themself.")
                print("By building a target audience primarily consisting of gullible 12 year olds,", name,
                      "rapidly climbs the ranks.")

                print("\nOne day,", name, "is approached by Mr. Beast and a plethora of their Youtube idols.")
                print("They wanted", name, 'to join their initiative coined "Team Trees."')

                print("\n" + name, "gladly accepts the offer.")

                print("\nTwo months later, Team Trees has successfully raised $20 million dollars, primarily thanks to",
                      name + ".")

                print("\nThrilled by their success, Youtube approaches", name,
                      "and offers them an irresistable job opportunity.")
                print("With this career,", name,
                      "would not only earn a hefty paycheck, but also have access to all of Youtube's data.")

                print("A few years into their career,", name, "is offered a deal by TRUMP.")
                print("In order to get re-elected, TRUMP wants to investigate his political rivals and", name,
                      "can get him that information.")

                print("\n" + name, "can either share Youtube's data (1) or stay out of TRUMP's blatent collusion (2)")

                # calls option function
                options(2)

                # data sanitation
                while validInput == False:
                    print("INVALID CHOICE")
                    options(2)

                # share Youtube's data
                if choice == "1":

                    separator()

                    print(name, "decides to share Youtube's data with TRUMP.")

                    print("The next day,", name, "hears banging on their front door.")
                    print('The banging subsides, but is replaced by a startling "FBI OPEN UP."')
                    print("With no intention to disobey the FBI,", name, "promptly opens the door.")

                    print("\n" + name, "is forcefully handcuffed and forced into the back of a black SUV.")

                    print("\nThe FBI had found out that", name, "had helped TRUMP collude.")
                    print(name, "is charged with obstruction of justice and is sentenced to life in prison.")

                    print("\nA pretty bad life...")

                    print("\n:(")

                    end()

                    playAgain()

                    # data sanitation
                    while validInput == False:
                        print("INVALID CHOICE")
                        playAgain()

                # stay out of TRUMP's blatent collusion
                else:

                    separator()

                    print(name, "decides to ignore TRUMP's requests.")

                    print("\nFurious, TRUMP lashes out on twitter about",
                          name + ", leaving out the collusion part, of course.")

                    print("\nMoments later,", name,
                          "receives a call from Youtube informing them that they have been fired.")

                    print("\n" + name, "lives out a pretty decent, average life.")
                    print("Although", name,
                          "didn't do much in their life time...at least they planted 20 million trees!")

                    end()

                    playAgain()

                    # data sanitation
                    while validInput == False:
                        print("INVALID CHOICE")
                        playAgain()

        # I'm feeling lucky
        else:

            separator()

            print(name, "is directed to a meme about TRUMP.")
            print("In fact, its the funniest meme that", name, "has ever seen.")
            print(name, "bursts out laughing.")

            print('\n"HAHAHAHAHAHAHAHA"')

            print("\nAfter a while,", name, "regains control of their funny bone.")

            print("\n" + name, "can send the meme to a friend (1) or set it as their background (2)")

            # calls option function
            options(2)

            # data sanitation
            while validInput == False:
                print("INVALID CHOICE")
                options(2)

                # send the meme to a friend
            if choice == "1":

                separator()

                print("\nIt turns out that the meme is also the funniest that", name + "'s friend has ever seen.")

                print("\n" + name, "spends the entire night chatting with their friend.")
                print(
                    "Their conversation jumps from politics to their favourite songs to how ready they are for winter break.")
                print("Naturally,", name,
                      "loses track of time and at 2 am (aka crackhead hours) they begin to doze off.")
                print(name, "has laughed more in this one night than their entire life.")

                print("\n...")

                print("\nHaving used up all of their energy,", name, "sleeps through the next day")
                print("...and the day after that")
                print("...and the day after that.")

                print("\nThat would be the last of", name + ".")
                print("The laughter inflicted by the meme was too much for", name + "'s body to handle.")

                print("\nHowever, the ramifications weren't contained to", name + ".")
                print(name + "'s friend would end up sharing the meme with even more friends.")
                print("In a chain reaction, the entire world was laughing...at a meme about TRUMP.")
                print("With the wave of laughter came a wave of eternal sleep.")

                print(
                    "\nNot climate change, not war, but a single meme was responsible for the extinction of the human race.")

                end()

                playAgain()

                # data sanitation
                while validInput == False:
                    print("INVALID CHOICE")
                    playAgain()

            # set it as their background
            else:

                separator()

                print("Plagued by the humor of the meme,", name, "starts to laugh uncontrollably again.")

                print("\n" + name, "feels immensely compelled to share their happiness with others.")
                print(name, "whips out their phone and sends it to their closest friend.")

                print("\nIt turns out that the meme is also the funniest that", name + "'s friend has ever seen.")

                print("\n" + name, "spends the entire night chatting with their friend.")
                print(
                    "Their conversation jumps from politics to their favourite songs to how ready they are for winter break.")
                print("Naturally,", name,
                      "loses track of time and at 2 am (aka crackhead hours) they begin to doze off.")
                print(name, "has laughed more in this one night than their entire life.")

                print("\n...")

                print("\nHaving used up all of their energy,", name, "sleeps through the next day")
                print("...and the day after that")
                print("...and the day after that.")

                print("\nThat would be the last of", name + ".")
                print("The laughter inflicted by the meme was too much for", name + "'s body to handle.")

                print("\nHowever, the ramifications weren't contained to", name + ".")
                print(name + "'s friend would end up sharing the meme with even more friends.")
                print("In a chain reaction, the entire world was laughing...at a meme about TRUMP.")
                print("With the wave of laughter came a wave of eternal sleep.")

                print(
                    "\nNot climate change, not war, but a single meme was responsible for the extinction of the human race.")

                end()

                playAgain()

                # data sanitation
                while validInput == False:
                    print("INVALID CHOICE")
                    playAgain()

# concluding remarks

print("Thank you for playing Michael's choose your own adventure game!")

print("\nI hope you enjoyed it!")

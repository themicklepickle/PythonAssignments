#Original Text (from the song, "You're Welcome")
"""
What can I say except you're welcome
For the tides, the sun, the sky
Hey, it's okay, it's okay
You're welcome
I'm just an ordinary demi-guy

Hey!
What has two thumbs that pulled up the sky
When you were waddling yay high
This guy!
"""

object1 = input("Enter an object: ")
object2 = input("Enter a second object: ")
object3 = input("Enter a third object: ")
adjective = input("Enter an adjective: ")
animal = input("Enter an animal: ")
number = input("Enter a number: ")
verb1 = input("Enter a verb in past tense: ")
verb2 = input("Enter a verb in present continuous tense: ")
bodyPart = input("Enter a body part in plural form: ")
interjection = input("Enter an interjection with the first letter capitalized: ")


print("\nWhat can I say except you're welcome\n",
      "For the ", object1, ", the ", object2, ", the ", object3, "\n",
      interjection, ", it's okay, it's okay\n",
      "You're welcome\n",
      "I'm just a ", adjective, " demi-", animal, "\n\n",
      interjection, "!", "\n",
      "What has ", number, " ", bodyPart, " that ", verb1, " up the sky\n",
      "When you were ", verb2, " yay high\n",
      "This ", animal, "!", sep = "")

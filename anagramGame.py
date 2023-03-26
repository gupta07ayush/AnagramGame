import random
import pyttsx3

i=pyttsx3.init() #object creation
i.setProperty('rate',150) # reducing the speech rate. Default is 200

name= input("Enter your name: ")

chances= 3
words=["starlord","groot","wolverine","daredevil","captainmarvel","blackwidow","hawkeys","wasp","antman","blade","ghost rider","hulk","blackpanther","captainamerica","ironman","thor","loki","wanda","vision","doctor strange","spiderman"]
word= random.choice(words)

jumble=''.join(random.sample(word,len(word)))
#print(jumble)


print("*"*180)
print("                                                            Avengers Jumble Game                                                    ")
print("*"*180)
print()
i.say("Hello " +name+ " Welcome to the Avenger game. Here, You will be given any Avenger name and you have total 3 chances to guess the correct avenger.")
i.runAndWait()


while chances != 0:
    print("The word is: ",jumble)
    guess = input("Enter your guessed word: ").lower()
    if guess == word:
        print("\nCorrect guess")
        print(name,"You won!")
        i.say("Congratulations"+name)
        i.runAndWait()
        break
    else:
        chances = chances-1
        print("\nincorrect guess")
        print("Remaining chances are: ",chances)
        
else:
    print("\nAll your chances are exhausted.")
    print(name+" You are a looser")
    i.say((name+" You are a looser \n")*5)
    print("The correct word is",word)
    i.runAndWait()
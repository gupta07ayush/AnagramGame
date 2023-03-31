import random
import pyttsx3
import time
import datetime

t = datetime.datetime.now()
t= t.hour

i=pyttsx3.init() #object creation
i.setProperty('rate',150) # reducing the speech rate. Default is 200

name= input("Enter your name: ")

chances= 3
words=["star lord","groot","wolverine","dare devil","captain marvel","black widow","hawk eye","wasp","ant man","blade","ghost rider","hulk","black panther","captain america","iron man","thor","loki","wanda","vision","doctor strange","spider man"]
str = random.choice(words)


# Split string into words
words = str.split()
#rint(words)


# shuffle = ["".join(random.sample(sp, len(i))) for i in sp ]
# jumble = "".join(shuffle)
# #jumble=''.join(random.sample(word,len(word)))   #for single word string

# Shuffle the letters of each word
shuffled_words = ["".join(random.sample(word, len(word))) for word in words]

# Join the shuffled words back into a string
jumble = " ".join(shuffled_words)


print(jumble)  #for testing


print("*"*150)
print("                                                            Avengers Jumble Game                                                    ")
print("*"*150)
print()
if t<12:
    print("I hope you are doing good",name)
    i.say(f"Good morning {name}")
elif 12 <= t < 18:
    print("Good Afternoon",name)
    i.say("Good AfterNoon",name)
else:
    print("Good Evening",name)  
    i.say("Good Evening",name)  
    
#i.say("Hello " +name+ " Welcome to the Avenger game. Here, You will be given any Avenger name and you have total 3 chances to guess the correct avenger.")
#i.runAndWait()


while chances != 0:
    print("The word is: ",jumble)
    start_time= time.perf_counter()
    s_time = time.perf_counter()
    guess = input("Enter your guessed word: ").lower()
    if guess == str:
        end_time=time.perf_counter()
        print("\nCorrect guess")
        print(name,"You won!")
        i.say("Congratulations"+name)
        print(f"Time taken =  {round(end_time - start_time)} seconds.")
        i.say(f"You took {round(end_time - start_time)} seconds to guess the correct Avenger. ")
        i.runAndWait()
        break
    else:
        chances = chances-1
        print("\nincorrect guess")
        print("Remaining chances are: ",chances)
        
else:
    end_time = time.perf_counter()
    print("\nAll your chances are exhausted.")
    print(f"You have wasted {round(end_time - s_time)} seconds.")
    print(name+" You are a looser")
    i.say((name+" You are a looser \n")*5)
    print("The correct word is",str)
    i.runAndWait()
import time

dateandtime = time.strftime("%d-%m-%Y %I:%M %p")
save_mode = "Not Selected Yet"
status = "In-Progress"

print()
print("Hello Riddle Master!")
print()
name = input("Your Name: ")
print("Which difficulty would you like?: 'Easy', 'Medium' or 'Hard'.")
d = input("Difficulty: ").lower()

if d == 'easy':
     save_mode = "Easy"
     print()
     print("Looks like you chose Easy Level!")
     print()
     print("Ok, you entered a park and there are these three swings: 'Seesaw', 'Merry Go Round' and 'Slide'.")
     print()
     print("If you want to ride these swings, answer this Riddle: ")
     seesaw_answer = input("Two sit side by side, one goes for a ride. When one's at the Top, the other must Drop. What Am I? Answer: ").lower()
     if seesaw_answer == "seesaw":
        status = "Win"
        print()
        print("Now you can take the Swings " + name + " !")
     elif seesaw_answer != "seesaw":
        status = "Lose"
        print()
        print("You lost the Easy Level! What a Shame " + name)

elif d == 'medium':
    save_mode = "Medium"
    print()
    print("Medium Level? Great Choice!")
    print()
    print("You have entered into a Maze!")
    print("Here's the riddle: 'What can go up and come down without moving?")
    temperature_answer = input("Answer: ").lower()
    if temperature_answer != "temperature":
        status = "Lose"
        print()
        print(name + ", you Lose and the answer was Temperature. ")
    elif temperature_answer == "temperature":
        print()
        print("Good Job! Now you have entered into a room and there is a riddle written inside the Room.")
        print()
        T = input("What starts with a 'T', ends with a 'T' and has 'T' in it? ").lower()
        if T != "teapot":
            status = "Lose"
            print()
            print("Sorry to say but you lost!")
        elif T == "teapot":
            print()
            print("Very well " + name + "! Now here's the last riddle. If you will do it correctly then you can escape!")
            print()
            S = input("What has holes but still holds water? ").lower()
            if S != "sponge":
                status = "Lose"
                print()
                print("Oh " + name + " It was the last riddle but you lost. The correct answer was 'Sponge'! ")
            elif S == "sponge":
                status = "Win"
                print()
                print("Excellent " + name + "! You Escaped!")




elif d == 'hard':
    save_mode = "Hard"
    print()
    print("Here is a swimming pool! let's dive in!")
    print()
    print()
    print("What! The swimming Pool is saying that you need to answer this riddle to get into it.")
    print()
    two = input("Here's the Riddle: 'I can be hot or cold, and I am found in lakes, rivers, and oceans. What am I?': ").lower()
    if two != "water":
        status = "Lose"
        print()
        print("Sorry " + name  + " Maybe you should try the Medium level!")
    elif two == "water":
        print()
        print("Nice! let's dive.")
        print()
        print("Oh no! there is a rock that's stopping us from going into the secret passage way! and this Question is written on it.....")
        print()
        three = input("What is the loudest Animal on Earth?: ").lower()
        if three != "whale":
            status = "Lose"
            print()
            print("Sorry, " + name + " Lose!")
        elif three == "whale":
            print()
            print("Yay!!!!" + name + " did it! Let's move forward!")
            print("Here's a riddle, be careful!")
            print()
            r1 = input("What is shaped like a box, has no feet, and runs up and down? (Hint: You use it in malls and supermarkets): ").lower()
            if r1 != "elevator":
                status = "Lose"
                print()
                print(name + ", You Lose!")
            elif r1 == "elevator":
                print()
                print("Yay! " + name + " You did it!")
                print()
                print("Now, we are going forward and there is another door with a riddle on it!")
                E = input("I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I? ").lower()
                if E != "echo":
                    status = "Lose"
                    print()
                    print(name + "lost. it's Answer was 'Echo'! I told you before that it is going to be HARD!")
                elif E == "echo":
                    print()
                    print("Wow " + name + "! You are a Riddle Master!")
                    print("Now here is a Question for you!")
                    print()
                    D = input("What is the Capital of Tajikistan?: ").lower()
                    if D != "dushanbe":
                        status = "Lose"
                        print()
                        print("It was an easy one but " + name + " lost. The Answer was 'Dushanbe!")
                    elif D == "dushanbe":
                        print()
                        print("Great, Now here's the last Question!")
                        M = input("What is the permanent natural satellite of the Earth? ").lower()
                        if M != "moon":
                            status = "Lose"
                            print()
                            print("Oh no! You lost and the Monster ate you up!")
                        elif M == "moon":
                            status = "Win"
                            print()
                            print("Yay!!!!!!!!!!!!!!!!! " + name + " Escaped!!! " + name + " has completed the Hard Level of the Riddle Adventure!")

# Saving the player names in a file called Guessy Integer Challenge players.txt
with open("Riddle Adventure players.txt", "a") as file:  # "a" is used for append
    file.write("Name: " + name + " || " + dateandtime + " || " + save_mode + " - " + status + "\n")
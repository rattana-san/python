#Guess + counting how many guesses

guess = 0
tries = 0
print("")
print("Let's play a game of guess the number")
print("")
while guess != 6:
    guess = int(input("Guess the number: "))
    tries += 1
    print("> number of tries: " + str(tries)) 
    print("")
if guess == 6:
    print("You did it!")
    print("")

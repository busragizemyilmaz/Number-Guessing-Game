import random

number = random.randint(0,100)
guess = None
count = 0

while guess != number:
    guess = int(input("Guess a number between 0 and 100 (You have 10 guesses!): "))
    count +=1

    if count < 10:
        if guess > number:  
            print("try lower again")

        elif guess < number:
            print("try higher again")

        else:
            print(f"CONGRATULATIONS!! You made {count} guesses")

    else:
        print("You lost because you exceeded your guess limit :(")
        break

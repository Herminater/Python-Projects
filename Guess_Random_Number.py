import random

guesses = 0 
number = random.randint(1,10)
print(number)


while guesses < 5:
    print(f"You have {5 - guesses} guesses left")
    guess = input("Guess: ")
    if int(guess) == number:
        print(f"Correct, the number was {number}")
        print("You win!")
        break
    elif guesses != 4:
        print("Wrong guess, try again. ")
        guesses += 1
    else:
        print("That is, unfortuneately, also wrong")
        print(f"You have no more guesses, the number was {number}")
        break



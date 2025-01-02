import random

Range_Top = input("Type for a range from 0 to n : ")

if Range_Top.isdigit():
    Range_Top = int(Range_Top)

    if Range_Top <= 0:
        print('Please type a number bigger than 0')
        quit()
else:
    print("Fucking type a number, dumbass")
    quit()


random_number = random.randint(0, Range_Top)
guess = 0

while True:
    guess+=1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("I said number, stupid")
        continue

    if user_guess == random_number:
        print('Correct!')
        break
    elif user_guess > random_number:
        print("Go lower")
    else:
        print("Go higher")

print("You made " , guess , " guesses")









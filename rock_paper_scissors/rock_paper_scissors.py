import random

user_score = 0
computer_score = 0
draw_score = 0

print("R = rock : P = paper : S = scissors : Q = quit -->")

options = ["r","p","s"]

while True:
    user_input = input("(R/P/S/Q) =  ").lower()
    user_input = user_input.lower()
    if user_input == "q":
        print("GGWP")
        break
    if user_input not in options:
        print("Error!Not a valid option!")
        continue

    random_number = random.randint(0, 2)
    # rock:0 paper:1 scissors:2
    computer_select = options[random_number]
    print("Computer chose", computer_select + ".")

    if user_input == computer_select:
        print("Draw!")
        draw_score+=1
        continue
    elif (user_input == "r" and computer_select == "s") or (user_input == "p" and computer_select == "r") or (user_input == "s" and computer_select == "p"):
        print("You win!")
        user_score+=1
    else:
        print("You lose!")
        computer_score+=1

    print(f"Score: You {user_score} - {computer_score} Computer")
    print(f"Draws: {draw_score}")


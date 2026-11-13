import random 
options = ("rock", "paper","scissors")

test_mode = True
fixed_choices = ["scissors","rock","paper"]

def get_winner(player,computer):
    if player == computer:
        return"draw"
    elif(player == "rock" and computer == "scissors") or\
        (player == "paper" and computer == "rock") or\
        (player == "scissors" and computer == "paper"):
        return"you win"
    else:
        return"computer wins"

playing = True

while playing:
    you = 0
    computer_score = 0
    draws = 0

    for round_no in range(3):

        if test_mode:
            computer = fixed_choices[round_no]
        else:
            computer = random.choice(options)

        invalid = False

        while True:
            player = input(f"round{round_no + 1} - Enter rock , paper or scissors:").lower().strip()
            if player in options:
                break

            print("invalid choice, Enter rock ,paper or scissors.")
            invalid = True

        result = get_winner(player , computer)

        if result == "you wins":
            you += 1
        elif result == "computer wins":
            computer_score += 1
        else:
            draws += 1

        if invalid and result == "you win":
            print(f"round{round_no + 1}:you win (no round lost)")
        else:
            print(f"round{round_no + 1}:result")

    print(f"You{you}|Computer {computer_score}|Draws{draws}")

    if you > computer_score:
        print("Result: you win!")
    elif computer_score > you:
        print("Result: computer win!")
    else:
        print("Result:draw!")

    again = input("play again?(yes/no):").lower().strip()

    if again != "yes":
        playing = False

print("thanks for playing")



        
        



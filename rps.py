import random
options = ["rock", "paper", "scissors"]
loop_running = True
while loop_running:
    user_answer = input("rock, paper, or scissors:\nyour answer: ").lower().strip()
    if user_answer == "rock":
        print("you chose rock")
    elif user_answer == "paper":
        print("you chose paper")
    elif user_answer == "scissors":
        print("you chose scissors")
    else:
        loop_running = False

    computer_pick = random.choice(options)
    print(computer_pick)
    if user_answer == computer_pick:
        print("still a failure")
    if user_answer == "rock":
        if computer_pick == "scissors":
            print("gg ez")
        if computer_pick == "paper":
            print("You're a failure")
    elif user_answer == "paper":
        if computer_pick == "rock":
            print("gg ez")
        if computer_pick == "scissors":
            print("You're a failure")
    elif user_answer == "scissors":
        if computer_pick == "paper":
            print("gg ez")
        if computer_pick == "rock":
            print("You're a failure")
from random import  choice
availableChoices = ["R", "P", "S"]

while True:
    user_choice = input("choose 'R' for Rock, 'P' for paper, 'S' for Scissors!\n ")
    cpu_player = choice(availableChoices)
    if user_choice in availableChoices:
        if user_choice == "R":
            if cpu_player == "R":
                print(f"Player({user_choice}):CPU({cpu_player})")
                print("It is a tie")
                continue
            elif cpu_player == "P":
                print(f"Player({user_choice}):CPU({cpu_player})")
                print("Oops You lost!")
                break
            elif cpu_player == "S":
                print(f"Player({user_choice}):CPU({cpu_player})")
                print("You won!")
                break
        elif user_choice == "P":
            if cpu_player == "R":
                print(f"Player({user_choice}):CPU({cpu_player})")
                print("You won!")
                break
            elif cpu_player == "P":
                print(f"Player({user_choice}):CPU({cpu_player})")
                print("It's a tie!")
                continue
            elif cpu_player == "S":
                print(f"Player({user_choice}):CPU({cpu_player})")
                print("Oops You lost!")
                break
        elif user_choice == "S":
            if cpu_player == "S":
                print(f"Player({user_choice}):CPU({cpu_player})")
                print("It's a tie!")
                continue
            elif cpu_player == "R":
                print(f"Player({user_choice}):CPU({cpu_player})")
                print("Oops You lost!")
                break
            elif cpu_player == "P":
                print(f"Player({user_choice}):CPU({cpu_player})")
                print("You won!")
                break
    else:
        print("Invalid command! Try again....")
        continue
import random


def rock():
    print("     ")
    print(" ___ ")
    print("/   \\")
    print("\___/")
    
    return "rock"


def paper():
    print("     ")
    print("-----")
    print("|   |")
    print("|   |")
    print("-----")
    
    return "paper"


def scissors():
    print("    ")
    print(" \ /")
    print("  X ")
    print(" O O")
    
    return "scissors"


def select_choice():
    choice_list = ["rock", "paper", "scissors"]

    choose_r_p_s = "placeholder"

    while not choose_r_p_s in choice_list:

        print("Available choices: 'rock', 'paper', 'scissors'")
        print("Shorthand choices: 'r', 'p', 's'")
        print()
        choose_r_p_s = input("Rock, Paper, Scissors, Shoot!: ").lower()
        print()

        if choose_r_p_s == "9":
            break

        print("Player 1: ")

        if choose_r_p_s[0] == "r":
            return "rock"

        if choose_r_p_s[0] == "p":
            
            return "paper"

        if choose_r_p_s[0] == "s":
            return "scissors"


def player(choice):
    if choice == "rock":
        return rock()

    if choice == "paper":
        return paper()

    if choice == "scissors":
        return scissors()


def cpu_choice():
    choice_list = ["rock", "paper", "scissors"]

    random_choice = random.choice(choice_list)

    print("CPU: ")

    if random_choice == "rock":
        return rock()

    if random_choice == "paper":
        return paper()

    if random_choice == "scissors":
        return scissors()


def replay():
    play_again = "placeholder"

    while not play_again == "y" and not play_again == "n":

        play_again = input("Would you like to play again? ")
        print()

        if play_again == "":
            continue

        if play_again[0] == "y":
            return True

        elif play_again[0] == "n":
            return False


def determine_winner(player_1, cpu):

    if player_1 == "rock" and cpu == "paper":
        print()
        print("CPU Wins!")
        return "cpu"
    elif player_1 == "paper" and cpu == "scissors":
        print()
        print("CPU Wins!")
        return "cpu"
    elif player_1 == "scissors" and cpu == "rock":
        print()
        print("CPU Wins!")
        return "cpu"
    elif cpu == "rock" and player_1 == "paper":
        print()
        print("Player 1 Wins!")
        return "p1"
    elif cpu == "paper" and player_1 == "scissors":
        print()
        print("Player 1 Wins!")
        return "p1"
    elif cpu == "scissors" and player_1 == "rock":
        print()
        print("Player 1 Wins!")
        return "p1"
    else:
        print()
        print("Tie.")


def score_tracker(p1_score, cpu_score):

    print()
    print("----------------------")
    print("| Player 1 |   CPU   |")
    print("----------------------")
    print("|   ",p1_score,"    |   ",cpu_score,"   |")
    print("----------------------")


def rock_paper_scissors_game():
    p1_score = 0
    cpu_score = 0

    game_on = True

    while game_on:

        player_1 = player(select_choice())
        print()
        print(" VS")
        print()
        cpu = cpu_choice()

        winner = determine_winner(player_1, cpu)

        if winner == "p1":
            p1_score += 1
        if winner == "cpu":
            cpu_score += 1

        score_tracker(p1_score, cpu_score)

        print()
        game_on = replay()


if __name__ == "__main__":
    rock_paper_scissors_game()

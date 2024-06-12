import random

# write 'hello world' to the console
print('hello world')
choices = ['rock', 'paper', 'scissors']
score = {'user': 0, 'computer': 0}

def play_game():
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors): ")
        if user_choice == 'exit':
            break
        elif user_choice == 'restart':
            reset_score()
            continue
        elif user_choice == 'help':
            print_instructions()
            continue
        elif user_choice == 'score':
            print_score()
            continue
        elif user_choice == 'reset':
            reset_score()
            continue
        
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            print("You win!")
            score['user'] += 1
        else:
            print("Computer wins!")
            score['computer'] += 1
    
    print("Game over.")

def reset_score():
    score['user'] = 0
    score['computer'] = 0
    print("Score reset.")

def print_instructions():
    print("""
    Instructions:
    - Enter 'rock', 'paper', or 'scissors' to make your choice.
    - Enter 'exit' to stop the game.
    - Enter 'restart' to restart the game.
    - Enter 'help' to get instructions.
    - Enter 'score' to get the current score.
    - Enter 'reset' to reset the score.
    """)

def print_score():
    print(f"Current score: User - {score['user']}, Computer - {score['computer']}")

play_game()


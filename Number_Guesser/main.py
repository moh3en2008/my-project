import random


def validate_input(User_guess):
    if not User_guess.isdigit():
        print('Invalid input. Please try again.')
        return False

    User_guess = int(User_guess)
    if User_guess > 100 or User_guess < 1:
        print('Your guess is out of range. Please try again. Your guess should be between 1 and 100.')
        return False
    
    return True


def start_game():
    rand_num = random.randint(1, 100)
    score = 100

    while True:
        User_guess = input("Guess a number between 1 and 100: ")

        if User_guess == 'q':
            print("Thank you for playing. Goodbye!")
            break

        if not validate_input(User_guess):
            continue

        User_guess = int(User_guess)
        if rand_num == User_guess:
            print('Congratulations! You guessed the correct number!')
            print(f"Your score is {score}.")
            wanna_play = input("Do you want to play again? (y/n): ")
            if wanna_play == 'y':
                start_game()
            else:
                print("Thank you for playing. Goodbye!")
                break
        
        
        elif rand_num > User_guess:
            print('Your guess is too low. please Try again!')
        else:
            print('Your guess is too high. please Try again!')
        
        score -= 10
        score = max(score, 0)


if __name__ == "__main__":
    start_game()

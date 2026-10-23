# (1) NUMBER GUESSING GAME

import random

def play_game():
    
    print('\nWElCOME to my "NUMBER GUESSING GAME" ')

    while True:
        choice = input("\nDo you want to play?  (Yes/No) ").strip().lower()

        if choice == "no":
            print("Okkay see yaa later :)")
            break
        elif choice != "yes":
            print("Kindly Enter yes or no only")
            continue

        print("\nLET'S START !! ")
        print(" • You have to guess the number between 1 to 100")
        print(" • You have 5 chances")
        print(" • Best of Luck :) ")

        secret_number = random.randint(1,100)     # selects a random number
        chances = 5

        while chances > 0:
            try:
                guess = int(input("\nEnter your guess: "))
            except ValueError:
                print("Enter valid number")
                continue

            if guess < 1 or guess > 100:
                print("You are out of Bounds!!")
                print("Enter numbers only between 1 and 100")
                continue

            chances -= 1

            if guess > secret_number:
                print(" • Try lower!")
                print(f" • Chances left: {chances}")
            elif guess < secret_number:
                print(" • Try higher!")
                print(f" • Chances left: {chances}")
            else:
                print("\n CONGRATULATIONS!!")
                print(" • You Guessed it correct\n ")
                break

        if chances == 0 and guess != secret_number:
            print("\nOOPS! Your chances are over :(")
            print(f" • The number was {secret_number}")

if __name__ == "__main__":
    play_game()






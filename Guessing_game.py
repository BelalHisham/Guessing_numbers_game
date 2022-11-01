from art import logo_guessing_game
import random
print(logo_guessing_game)
print("welcome to Number Guessing game")
print("I am thinking of a number between 1 and 100")

the_number = random.randint(1,100)
# print(the_number)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
num_of_attemps = 0
if difficulty == "easy":
    num_of_attemps = 10
elif difficulty == "hard":
    num_of_attemps = 5
else:
    print("Invalid input")


print(f"You hve {num_of_attemps} attemps")

user_guess = int( input("Make a guess: "))


game_finished = False
while not game_finished:
    if num_of_attemps == 0:
        print(f"You lost the answer was {num_of_attemps}")
        game_finished = True
    elif user_guess > the_number:
        print("Too High")
        num_of_attemps -= 1
        if num_of_attemps != 0:
            print(f"You have {num_of_attemps} attemps remaining")
            user_guess = int( input("Make a guess: "))
    elif user_guess < the_number:
        print("Too Low")
        num_of_attemps -= 1
        if num_of_attemps != 0:
            print(f"You have {num_of_attemps} attemps remaining")
            user_guess = int( input("Make a guess: "))
    elif user_guess == the_number:
        print(f"You won!! the answer was {num_of_attemps}")
        game_finished = True
    
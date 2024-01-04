from game_data import data
import random
from art import vs, logo

def random_data(accounts):
    """A func to generate random data from game data"""
    name = accounts["name"]
    description = accounts["description"]
    country = accounts["country"]
    return (f"{name}, a {description} from {country}.")

def checking_ans (account_a,account_b, guess):
    """Func to check followers count"""
    for_acc_a = account_a ["follower_count"]
    for_acc_b = account_b ["follower_count"]

    if for_acc_a > for_acc_b:
        return guess == "a"
    else:
        return guess == "b"
    
print (logo)
score = 0
account_b = random.choice (data)

game_not_ends = True

while game_not_ends:
    account_a = account_b
    account_b = random.choice (data)
    while account_a == account_b:
        account_b = random.choice (data)


    for_a = random_data(account_a)
    for_b = random_data(account_b)

    print (f"Compare A: {for_a}")
    print (vs)
    print (f"Against B: {for_b}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    main_game = checking_ans(account_a,account_b, guess)
    if main_game == True:
        score += 1
        print (f"Correct. Your current score is {score}")
    else:
        print (f"you lose. Your final score is {score}")
        game_not_ends = False


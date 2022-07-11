from art import logo, vs
from game_data import data
import random

def formate_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]

    return f"{account_name}, a {account_descr}, from{account_country}"

def check_answer(guess, a_follwers, b_followers):
    if a_follwers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'

score = 0
should_continue = False

while not should_continue:
    account_a = random.choice(data)
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {formate_data(account_a)}")
    print(vs)
    print(f"Against B: {formate_data(account_a)}")
    guess = input("Who has more follower. Type 'a' or 'b': ")

    follower_count_a = account_a["follower_count"]
    follower_count_b = account_b["follower_count"]
    correct = check_answer(guess, follower_count_a, follower_count_b)

    if correct:
        score += 1
        print(f"You are right. Current score is: {score}.")
    else:
        should_continue = True
        print("You are wrong. Final score is: {score}.")








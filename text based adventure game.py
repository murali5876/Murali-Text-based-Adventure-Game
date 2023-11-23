import time
import random
from colorama import Fore, Style, init

init(autoreset=True)

class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.coins = 0
        self.health = 100

def introduction():
    print(Fore.CYAN + "Welcome to the REALM OF LEGEND'S!" + Style.RESET_ALL)
    time.sleep(1)
    print("You find yourself in a mysterious land...")
    time.sleep(1)
    print("Your choices will shape your destiny. Let the epic adventure unfold!\n")

def get_player_name():
    name = input(Fore.YELLOW + "Enter your character's name: " + Style.RESET_ALL)
    return name

def make_choice(choices):
    print(Fore.GREEN + "Choose your path:" + Style.RESET_ALL)
    for index, choice in enumerate(choices, start=1):
        print(f"{Fore.MAGENTA}{index}. {choice}" + Style.RESET_ALL)

    while True:
        try:
            user_input = int(input(Fore.YELLOW + "Enter the number of your choice: " + Style.RESET_ALL))
            if 1 <= user_input <= len(choices):
                return user_input
            else:
                print(Fore.RED + "Invalid choice. Please enter a valid number." + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a number." + Style.RESET_ALL)

def explore_cave(player):
    print("You enter a dark cave...")
    time.sleep(1)
    print("You see two paths ahead.")
    choices = ["Take the left path", "Take the right path"]
    user_choice = make_choice(choices)

    if user_choice == 1:
        print("You encounter a friendly creature. It offers you a healing potion.")
        player.inventory.append("Healing Potion")
        print("You added a Healing Potion to your inventory.")
    else:
        print("You face a challenging obstacle. After overcoming it, you find a hidden treasure.")
        player.inventory.append("Treasure Chest")
        print("You added a Treasure Chest to your inventory.")

def face_dragon(player):
    print("You find yourself in front of a mighty dragon!")
    time.sleep(1)
    print("What will you do?")
    choices = ["Fight the dragon", "Try to sneak past", "Attempt to negotiate"]
    user_choice = make_choice(choices)

    if user_choice == 1:
        if "Sword" in player.inventory and "Shield" in player.inventory:
            print("You bravely fight the dragon...")
            time.sleep(1)
            print("With your mighty sword and sturdy shield, you defeat the dragon!")
            print("Congratulations! You've successfully completed the adventure!")
        else:
            print("You need both a sword and a shield to win the battle. Explore more to find them.")
            return False
    elif user_choice == 2:
        print("You attempt to sneak past, but the dragon senses your presence.")
        time.sleep(1)
        print(Fore.RED + "Game Over. The dragon catches you!" + Style.RESET_ALL)
        exit()
    else:
        print("You wisely negotiate with the dragon and gain its assistance.")
        time.sleep(1)
        print("The dragon becomes your ally. You've successfully completed the adventure!")
    return True

def earn_coins(player):
    print("You choose to earn coins by answering mathematical questions.")
    time.sleep(1)
    
    # Generate a random mathematical question
    num1 = random.randint(1, 99)
    num2 = random.randint(1, 99)
    
    question = f"What is {num1} + {num2}?"
    user_answer = input(Fore.YELLOW + f"{question} " + Style.RESET_ALL)

    # Check if the answer is correct
    correct_answer = num1 + num2
    if user_answer.isdigit() and int(user_answer) == correct_answer:
        earned_coins = random.randint(1, 10)
        player.coins += earned_coins
        print(f"Correct! You earned {earned_coins} coins.")
        print(f"{Fore.YELLOW}Total Coins: {player.coins}" + Style.RESET_ALL)
    else:
        print(Fore.RED + "Incorrect answer. No coins earned." + Style.RESET_ALL)

def village_market(player):
    print("You arrive at a bustling village market...")
    time.sleep(1)
    print("You can buy items here to aid you on your journey.")
    
    sword_price = 5  # Cost of Sword in coins
    shield_price = 3  # Cost of Shield in coins
    
    choices = [
        f"Buy a Sword (Cost: {sword_price} coins)",
        f"Buy a Shield (Cost: {shield_price} coins)",
        "Leave the market"
    ]
    user_choice = make_choice(choices)

    if user_choice == 1:
        if player.coins >= sword_price:
            print("You purchase a mighty Sword.")
            player.inventory.append("Sword")
            print("You added a Sword to your inventory.")
            player.coins -= sword_price
            print(f"{Fore.YELLOW}Coins remaining: {player.coins}" + Style.RESET_ALL)
        else:
            print(Fore.RED + "You don't have enough coins to buy the Sword. Earn more coins!" + Style.RESET_ALL)
    elif user_choice == 2:
        if player.coins >= shield_price:
            print("You purchase a sturdy Shield.")
            player.inventory.append("Shield")
            print("You added a Shield to your inventory.")
            player.coins -= shield_price
            print(f"{Fore.YELLOW}Coins remaining: {player.coins}" + Style.RESET_ALL)
        else:
            print(Fore.RED + "You don't have enough coins to buy the Shield. Earn more coins!" + Style.RESET_ALL)
    else:
        print("You decide to leave the market.")

def main():
    introduction()
    
    player_name = get_player_name()
    player = Player(player_name)

    print(f"Hello, {Fore.GREEN}{player.name}!{Style.RESET_ALL} Your adventure begins.")

    dragon_won = False  # Flag to check if the player won against the dragon

    while True:
        print("\nOptions:")
        print(f"{Fore.MAGENTA}1. Explore the dark cave" + Style.RESET_ALL)
        print(f"{Fore.MAGENTA}2. Face the mighty dragon" + Style.RESET_ALL)
        print(f"{Fore.MAGENTA}3. Earn Coins" + Style.RESET_ALL)
        print(f"{Fore.MAGENTA}4. Visit the village market" + Style.RESET_ALL)
        print(f"{Fore.MAGENTA}5. View Inventory" + Style.RESET_ALL)
        print(f"{Fore.MAGENTA}6. Exit the game" + Style.RESET_ALL)

        user_choice = make_choice(["Explore", "Face Dragon", "Earn Coins", "Visit Market", "Inventory", "Exit"])

        if user_choice == 1:
            explore_cave(player)
        elif user_choice == 2:
            dragon_won = face_dragon(player)
        elif user_choice == 3:
            earn_coins(player)
        elif user_choice == 4:
            village_market(player)
        elif user_choice == 5:
            print("Inventory:")
            for item in player.inventory:
                print(f"{Fore.CYAN}- {item}" + Style.RESET_ALL)
            print(f"{Fore.YELLOW}Coins: {player.coins}" + Style.RESET_ALL)
        else:
            if dragon_won:
                print(Fore.RED + "Exiting the game. Thanks for playing!" + Style.RESET_ALL)
                break
            else:
                print(Fore.RED + "You cannot exit before winning the fight against the dragon!" + Style.RESET_ALL)

if __name__ == "__main__":
    main()

import random
import time

class NFT:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class Player:
    def __init__(self, name):
        self.name = name
        self.balance = 1000
        self.inventory = []

    def buy_nft(self, nft):
        if self.balance >= nft.value:
            self.balance -= nft.value
            self.inventory.append(nft)
            return True
        else:
            return False

    def sell_nft(self, nft):
        if nft in self.inventory:
            self.balance += nft.value
            self.inventory.remove(nft)
            return True
        else:
            return False

def trigger_random_event():
    events = [
        "Market Bull Run",
        "Market Crash",
        "Limited-Time Offer",
        "Hacker Attack",
        "NFT Airdrop",
        "Market Stabilization",
    ]
    selected_event = random.choice(events)
    return selected_event

def handle_event(event, player):
    if event == "Market Bull Run":
        increase_nft_prices(player.inventory)
        print("A market bull run has occurred! NFT prices are soaring.")
    elif event == "Market Crash":
        decrease_nft_prices(player.inventory)
        print("A market crash has occurred! NFT prices are plummeting.")
    elif event == "Limited-Time Offer":
        offer_discount(player)
        print("A limited-time offer is available! NFTs are at a discount.")

def increase_nft_prices(nft_list):
    for nft in nft_list:
        nft.value += random.randint(10, 100)

def decrease_nft_prices(nft_list):
    for nft in nft_list:
        nft.value -= random.randint(10, 100)
        if nft.value < 0:
            nft.value = 0

def offer_discount(player):
    discount = random.randint(10, 30)
    for nft in player.inventory:
        nft.value -= discount
        if nft.value < 0:
            nft.value = 0

def main():
    player_name = input("Enter your name: ")
    player = Player(player_name)

    while True:
        print("\nWelcome to the NFT Trading Game!")
        print(f"Player: {player.name}, Balance: {player.balance} coins")
        print("Your Inventory:")
        for i, nft in enumerate(player.inventory):
            print(f"{i + 1}. {nft.name} ({nft.value} coins)")

        print("\nAvailable NFTs:")
        for i, nft in enumerate(nft_catalog):
            print(f"{i + 1}. {nft.name} ({nft.value} coins)")

        event_chance = random.randint(1, 100)
        if event_chance <= 99:
            event = trigger_random_event()
            handle_event(event, player)

        choice = input("Enter 'buy' or 'sell' or 'quit': ").lower()

        if choice == "quit":
            break
        elif choice == "buy":
            nft_choice = int(input("Enter the NFT number you want to buy: "))
            if nft_choice >= 1 and nft_choice <= len(nft_catalog):
                success = player.buy_nft(nft_catalog[nft_choice - 1])
                if success:
                    print("Purchase successful!")
                else:
                    print("Insufficient balance.")
            else:
                print("Invalid choice.")
        elif choice == "sell":
            if len(player.inventory) == 0:
                print("You have no NFTs to sell.")
            else:
                nft_choice = int(input("Enter the NFT number you want to sell: "))
                if nft_choice >= 1 and nft_choice <= len(player.inventory):
                    success = player.sell_nft(player.inventory[nft_choice - 1])
                    if success:
                        print("Sale successful!")
                    else:
                        print("Invalid choice.")
                else:
                    print("Invalid choice.")

if __name__ == "__main__":
    nft_catalog = [
        NFT("Dragon Sword", 500),
        NFT("Magic Ring", 300),
        NFT("Golden Crown", 800),
    ]

    main()

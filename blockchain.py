blockchain = []

def get_last_blockchain_value():
    """ Gets the last element of the chain """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_value(transaction_amount, last_transaction = [1]):
    """ Append a new value as well as the last blockchain value to the blockchain"""
    blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    """ Get the value entered by the user as a Float """
    return float(input("Your transaction amount please: "))


def get_user_choice():
    """ Get the user choice """
    return input("Your choice: ")


def print_blockchain_elements():
    for block in blockchain:
        print(block)


while True:
    print("\nPlease choose one option")
    print("1: Add a new transaction value")
    print("2: Output the blockchain blocks")
    print("q: Quit")
    user_choice = get_user_choice()
    if user_choice == "1":
        tx_amout = get_transaction_value()
        add_value(last_transaction = get_last_blockchain_value(), transaction_amount = tx_amout)
    elif user_choice == "2":
        print_blockchain_elements()
    elif user_choice == "q":
        break
    else:
        print("Input invalid, please pick a valid option")
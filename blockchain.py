blockchain = []

def get_last_blockchain_value():
    """ Gets the last element of the chain """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_value(transaction_amount, last_transaction):
    """ Append a new value as well as the last blockchain value to the blockchain"""
    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])


def get_transaction():
    """ Get the value entered by the user as a Float """
    return float(input("Your transaction amount please: "))


def get_user_choice():
    """ Get the user choice """
    return input("Your choice: ")


def print_blockchain_elements():
    for block in blockchain:
        print(block)
    else:
        print("-" * 20)


def verify_chain():
    block_index = 0
    is_valid = True
    for block in blockchain:
        if block_index == 0:
            block_index += 1
            continue
        if block[0] != blockchain[block_index - 1]:
            is_valid = False
            break
        block_index += 1
    return is_valid

waiting_for_input = True

while waiting_for_input:
    print("\nPlease choose one option")
    print("1: Add a new transaction value")
    print("2: Output the blockchain blocks")
    print("h: Manipulate the blockchain")
    print("v: Verify chain")
    print("q: Quit")
    user_choice = get_user_choice()
    if user_choice == "1":
        tx_amout = get_transaction()
        add_value(last_transaction = get_last_blockchain_value(), transaction_amount = tx_amout)
    elif user_choice == "2":
        print_blockchain_elements()
    elif user_choice == "h":
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == "v":
        verify_chain()
    elif user_choice == "q":
        waiting_for_input = False
    else:
        print("Input invalid, please pick a valid option")
    if not verify_chain():
        print("Invalid blockchain!")
        waiting_for_input = False
else:
    print("User left")

print("Done")
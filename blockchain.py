genesis_block = {
    "previous_hash": "",
    "index": 0,
    "transactions": []
}
blockchain = [genesis_block]
open_transactions = []
owner = "Guilherme"
participants = {"Guilherme"}

def hash_block(block):
    return "-".join([str(block[key]) for key in block])


def get_last_blockchain_value():
    """ Gets the last element of the chain """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(recipient, sender=owner, amount=1.0):
    """ Append a new value as well as the last blockchain value to the blockchain"""
    transaction = {
        "sender": sender,
        "recipient": recipient,
        "amount": amount
    }
    open_transactions.append(transaction)
    participants.add(sender)
    participants.add(recipient)


def mine_block():
    block_hash = hash_block(blockchain[-1])
    block = {
        "previous_hash": block_hash,
        "index": len(blockchain),
        "transactions": open_transactions
    }
    blockchain.append(block)
    return True


def get_transaction_value():
    """ Get the value entered by the user as a Float """
    tx_recipient = input("Enter the recipient of the transaction: ")
    tx_amount = float(input("Your transaction amount please: "))
    return tx_recipient, tx_amount


def get_user_choice():
    """ Get the user choice """
    return input("Your choice: ")


def print_blockchain_elements():
    for block in blockchain:
        print(block)
    else:
        print("-" * 20)


def verify_chain():
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block["previous_hash"] != hash_block(blockchain[index - 1]):
            return False
    return True


waiting_for_input = True

while waiting_for_input:
    print("\nPlease choose one option")
    print("1: Add a new transaction value")
    print("2: Minea new block")
    print("3: Output the blockchain blocks")
    print("4: Output participants")
    print("h: Manipulate the blockchain")
    print("v: Verify chain")
    print("q: Quit")
    user_choice = get_user_choice()
    if user_choice == "1":
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        add_transaction(recipient, amount=amount)
        print(open_transactions)
    elif user_choice == "2":
        if mine_block():
            open_transactions = []
    elif user_choice == "3":
        print_blockchain_elements()
    elif user_choice == "4":
        print(participants)
    elif user_choice == "h":
        if len(blockchain) >= 1:
            blockchain[0] = {
                "previous_hash": "",
                "index": 0,
                "transactions": [{
                    "sender": "Max",
                    "recipient": "Gustavo Luiz",
                    "amount": 10.0
                }]
            }
    elif user_choice == "v":
        verify_chain()
    elif user_choice == "q":
        waiting_for_input = False
    else:
        print("Input invalid, please pick a valid option")
    if not verify_chain():
        print_blockchain_elements()
        print("Inválid blockchain")
        break
else:
    print("User left")

print("Done")
import functools

MINING_REWARD = 10

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


def get_balance(participant):
    tx_sender = [[tx["amount"] for tx in block["transactions"] if tx["sender"] == participant] for block in blockchain]
    open_tx_sender = [tx["amount"] for tx in open_transactions if tx["sender"] == participant]

    tx_sender.append(open_tx_sender)
    amount_sent = functools.reduce(lambda tx_sum, tx_amount: tx_sum + sum(tx_amount) if len(tx_amount) > 0 else tx_sum + 0, tx_sender, 0)

    tx_recipient = [[tx["amount"] for tx in block["transactions"] if tx["recipient"] == participant] for block in blockchain]
    amount_recived = functools.reduce(lambda tx_sum, tx_amount: tx_sum + sum(tx_amount) if len(tx_amount) > 0 else tx_sum + 0, tx_recipient, 0)

    return amount_recived - amount_sent


def get_last_blockchain_value():
    """ Gets the last element of the chain """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def verify_transaction(transaction):
    sender_balance = get_balance(transaction["sender"])
    return sender_balance >= transaction["amount"]


def verify_transactions():
    return all([verify_transaction(tx) for tx in open_transactions])


def add_transaction(recipient, sender=owner, amount=1.0):
    """ Append a new value as well as the last blockchain value to the blockchain"""
    transaction = {
        "sender": sender,
        "recipient": recipient,
        "amount": amount
    }
    if verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        return True
    else:
        return False


def mine_block():
    block_hash = hash_block(blockchain[-1])
    reward_transaction = {
        "sender": "MINING",
        "recipient": owner,
        "amount": MINING_REWARD
    }
    copied_transactions = open_transactions[:]
    copied_transactions.append(reward_transaction)
    block = {
        "previous_hash": block_hash,
        "index": len(blockchain),
        "transactions": copied_transactions
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
    print("5: Check transaction validity")
    print("h: Manipulate the blockchain")
    print("v: Verify chain")
    print("q: Quit")
    user_choice = get_user_choice()
    if user_choice == "1":
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        if add_transaction(recipient, amount=amount):
            print("Transaction succeded")
        else:
            print("Transcation failed")
        print(open_transactions)
    elif user_choice == "2":
        if mine_block():
            open_transactions = []
    elif user_choice == "3":
        print_blockchain_elements()
    elif user_choice == "4":
        print(participants)
    elif user_choice == "5":
        if verify_transactions():
            print("all valid")
        else:
            print("Not all valid")
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
    print("Balance of {}: {:6.2f}".format("Guilherme", get_balance("Guilherme")))
else:
    print("User left")

print("Done")
import functools
import hashlib
import json
import pickle

from hash_util import hash_block
from block import Block
from transaction import Transaction
from verification import Verification

MINING_REWARD = 10
blockchain = []
open_transactions = []
owner = "Guilherme"
participants = {"Guilherme"}


def save_data():
    try:
        with open('blockchain.txt', mode='w') as f:
            saveble_blockchain = [block.__dict__ for block in [Block(block_el.index, block_el.previous_hash, [
                                                                     tx.__dict__ for tx in block_el.transactions], block_el.proof, block_el.timestamp) for block_el in blockchain]]
            f.write(json.dumps(saveble_blockchain))
            f.write('\n')
            saveble_tx = [tx.__dict__ for tx in open_transactions]
            f.write(json.dumps(saveble_tx))
            # save_data = {
            #     "chain": blockchain,
            #     "ot": open_transactions
            # }
            # f.write(pickle.dumps(save_data))
    except IOError:
        print('Saving failed')


def load_data():
    global blockchain
    global open_transactions
    try:
        with open('blockchain.txt', mode='r') as f:
            # data = pickle.loads(f.read())
            # global blockchain
            # global open_transactions
            # blockchain = data["chain"]
            # open_transactions = data["ot"]
            file_contents = f.readlines()
            blockchain = json.loads(file_contents[0][:-1])
            updated_blockchain = []
            for block in blockchain:
                converted_tx = [Transaction(
                    tx["sender"], tx["recipient"], tx["amount"]) for tx in block["transactions"]]
                updated_block = Block(
                    block['index'], block['previous_hash'], converted_tx, block['proof'], block['timestamp'])
                updated_blockchain.append(updated_block)

            blockchain = updated_blockchain

            open_transactions = json.loads(file_contents[1])
            updated_transactions = []
            for tx in open_transactions:
                updated_transaction = Transaction(
                    tx["sender"], tx["recipient"], tx["amount"])
                updated_transactions.append(updated_transaction)
            open_transactions = updated_transactions
    except (IOError, IndexError):
        genesis_block = Block(0, "", [], 100)
        blockchain = [genesis_block]
        open_transactions = []
    finally:
        print('Cleanup')


load_data()


def proof_of_work():
    last_block = blockchain[-1]
    last_hash = hash_block(last_block)
    proof = 0
    verifier = Verification()
    while not verifier.valid_proof(open_transactions, last_hash, proof):
        proof += 1
    return proof


def get_balance(participant):
    tx_sender = [[tx.amount for tx in block.transactions if tx.sender ==
                  participant] for block in blockchain]
    open_tx_sender = [
        tx.amount for tx in open_transactions if tx.sender == participant]

    tx_sender.append(open_tx_sender)
    amount_sent = functools.reduce(lambda tx_sum, tx_amount: tx_sum + sum(
        tx_amount) if len(tx_amount) > 0 else tx_sum + 0, tx_sender, 0)

    tx_recipient = [[tx.amount for tx in block.transactions if tx.recipient ==
                     participant] for block in blockchain]
    amount_recived = functools.reduce(lambda tx_sum, tx_amount: tx_sum + sum(
        tx_amount) if len(tx_amount) > 0 else tx_sum + 0, tx_recipient, 0)

    return amount_recived - amount_sent


def get_last_blockchain_value():
    """ Gets the last element of the chain """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(recipient, sender=owner, amount=1.0):
    """ Append a new value as well as the last blockchain value to the blockchain"""
    transaction = Transaction(sender, recipient, amount)
    verifier = Verification()
    if verifier.verify_transaction(transaction, get_balance):
        open_transactions.append(transaction)
        save_data()
        return True
    return False


def mine_block():
    block_hash = hash_block(blockchain[-1])
    proof = proof_of_work()
    reward_transaction = Transaction("MINING", owner, MINING_REWARD)
    copied_transactions = open_transactions[:]
    copied_transactions.append(reward_transaction)
    block = Block(len(blockchain), block_hash, copied_transactions, proof)
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


waiting_for_input = True

while waiting_for_input:
    verifier = Verification()
    print("\nPlease choose one option")
    print("1: Add a new transaction value")
    print("2: Mine a new block")
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
            save_data()
    elif user_choice == "3":
        print_blockchain_elements()
    elif user_choice == "4":
        print(participants)
    elif user_choice == "5":
        if verifier.verify_transactions(open_transactions, get_balance):
            print("all valid")
        else:
            print("Not all valid")
    elif user_choice == "q":
        waiting_for_input = False
    else:
        print("Input invalid, please pick a valid option")
    if not verifier.verify_chain(blockchain):
        print_blockchain_elements()
        print("Inválid blockchain")
        break
    print("Balance of {}: {:6.2f}".format(
        "Guilherme", get_balance("Guilherme")))
else:
    print("User left")

print("Done")
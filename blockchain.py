blockchain = []

def get_last_blockchain_value():
    """ Gets the last element of the chain """
    return blockchain[-1]


def add_value(transaction_amount, last_transaction = [1]):
    """ Append a new value as well as the last blockchain value to the blockchain"""
    blockchain.append([last_transaction, transaction_amount])


def get_user_input():
    """ Get the value entered by the user as a Float """
    return float(input("Your transaction amount please: "))

tx_amout = get_user_input()
add_value(tx_amout)

tx_amout = get_user_input()
add_value(last_transaction = get_last_blockchain_value(), transaction_amount = tx_amout)

tx_amout = get_user_input()
add_value(tx_amout, get_last_blockchain_value())

print(blockchain)
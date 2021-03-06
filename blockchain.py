import functools
import hashlib
import json
import pickle

from utility.hash_util import hash_block
from utility.verification import Verification
from block import Block
from transaction import Transaction
from wallet import Wallet

MINING_REWARD = 10
blockchain = []
participants = {"Guilherme"}

class Blockchain:
    def __init__(self, hosting_node):
        genesis_block = Block(0, "", [], 100)
        self.chain = [genesis_block]
        self.__open_transactions = []
        self.load_data()
        self.hosting_node = hosting_node


    @property
    def chain(self):
        return self.__chain[:]


    @chain.setter
    def chain(self, val):
        self.__chain = val


    def get_open_transactions(self):
        return self.__open_transactions.copy()


    def save_data(self):
        try:
            with open('blockchain.txt', mode='w') as f:
                saveble_blockchain = [block.__dict__ for block in [Block(block_el.index, block_el.previous_hash, [
                                                                        tx.__dict__ for tx in block_el.transactions], block_el.proof, block_el.timestamp) for block_el in self.__chain]]
                f.write(json.dumps(saveble_blockchain))
                f.write('\n')
                saveble_tx = [tx.__dict__ for tx in self.__open_transactions]
                f.write(json.dumps(saveble_tx))
                # save_data = {
                #     "chain": blockchain,
                #     "ot": open_transactions
                # }
                # f.write(pickle.dumps(save_data))
        except IOError:
            print('Saving failed')


    def load_data(self):
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
                        tx["sender"], tx["recipient"], tx["signature"], tx["amount"]) for tx in block["transactions"]]
                    updated_block = Block(
                        block['index'], block['previous_hash'], converted_tx, block['proof'], block['timestamp'])
                    updated_blockchain.append(updated_block)

                self.__chain = updated_blockchain

                open_transactions = json.loads(file_contents[1])
                updated_transactions = []
                for tx in open_transactions:
                    updated_transaction = Transaction(
                        tx["sender"], tx["recipient"], tx["signature"], tx["amount"])
                    updated_transactions.append(updated_transaction)
                self.__open_transactions = updated_transactions
        except (IOError, IndexError):
            print('Handled exception')
        finally:
            print('Cleanup')


    def proof_of_work(self):
        last_block = self.__chain[-1]
        last_hash = hash_block(last_block)
        proof = 0
        while not Verification.valid_proof(self.__open_transactions, last_hash, proof):
            proof += 1
        return proof


    def get_balance(self):
        if self.hosting_node == None:
            return None
        tx_sender = [[tx.amount for tx in block.transactions if tx.sender ==
                    self.hosting_node] for block in self.__chain]
        open_tx_sender = [
            tx.amount for tx in self.__open_transactions if tx.sender == self.hosting_node]

        tx_sender.append(open_tx_sender)
        amount_sent = functools.reduce(lambda tx_sum, tx_amount: tx_sum + sum(
            tx_amount) if len(tx_amount) > 0 else tx_sum + 0, tx_sender, 0)

        tx_recipient = [[tx.amount for tx in block.transactions if tx.recipient ==
                        self.hosting_node] for block in self.__chain]
        amount_recived = functools.reduce(lambda tx_sum, tx_amount: tx_sum + sum(
            tx_amount) if len(tx_amount) > 0 else tx_sum + 0, tx_recipient, 0)

        return amount_recived - amount_sent


    def get_last_blockchain_value(self):
        """ Gets the last element of the chain """
        if len(self.__chain) < 1:
            return None
        return self.__chain[-1]


    def add_transaction(self, recipient, sender, signature, amount=1.0):
        """ Append a new value as well as the last blockchain value to the blockchain"""
        if self.hosting_node == None:
            return False

        transaction = Transaction(sender, recipient, signature, amount)
        if Verification.verify_transaction(transaction, self.get_balance):
            self.__open_transactions.append(transaction)
            self.save_data()
            return True
        return False


    def mine_block(self):
        if self.hosting_node == None:
            return None

        block_hash = hash_block(self.__chain[-1])
        proof = self.proof_of_work()
        reward_transaction = Transaction("MINING", self.hosting_node, '', MINING_REWARD)
        copied_transactions = self.__open_transactions[:]
        for tx in copied_transactions:
            if not Wallet.verify_transaction(tx):
                return None
        copied_transactions.append(reward_transaction)
        block = Block(len(self.__chain), block_hash, copied_transactions, proof)
        self.__chain.append(block)
        self.__open_transactions = []
        self.save_data()
        return block
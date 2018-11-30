from blockchain import Blockchain
from wallet import Wallet
from utility.verification import Verification

from uuid import uuid4

class Node:
    def __init__(self):
        self.wallet = Wallet()
        # self.blockchain = None
        self.blockchain = Blockchain(self.wallet.public_key)

    def get_transaction_value(self):
        """ Get the value entered by the user as a Float """
        tx_recipient = input("Enter the recipient of the transaction: ")
        tx_amount = float(input("Your transaction amount please: "))
        return tx_recipient, tx_amount


    def get_user_choice(self):
        """ Get the user choice """
        return input("Your choice: ")


    def print_blockchain_elements(self):
        for block in self.blockchain.chain:
            print(block)
        else:
            print("-" * 20)


    def listem_for_input(self):
        waiting_for_input = True

        while waiting_for_input:
            print("\nPlease choose one option")
            print("1: Add a new transaction value")
            print("2: Mine a new block")
            print("3: Output the blockchain blocks")
            print("4: Check transaction validity")
            print("5: Create wallet")
            print("6: Load wallet")
            print("7: Save wallet")
            print("h: Manipulate the blockchain")
            print("v: Verify chain")
            print("q: Quit")
            user_choice = self.get_user_choice()
            if user_choice == "1":
                tx_data = self.get_transaction_value()
                recipient, amount = tx_data
                signature = self.wallet.sign_transaction(self.wallet.public_key, recipient, amount)
                if self.blockchain.add_transaction(recipient, self.wallet.public_key, signature, amount=amount):
                    print("Transaction succeded")
                else:
                    print("Transcation failed")
                print(self.blockchain.get_open_transactions())
            elif user_choice == "2":
                if not self.blockchain.mine_block():
                    print("Mining failed. Got no wallet?")
            elif user_choice == "3":
                self.print_blockchain_elements()
            elif user_choice == "4":
                if Verification.verify_transactions(self.blockchain.get_open_transactions(), self.blockchain.get_balance):
                    print("all valid")
                else:
                    print("Not all valid")
            elif user_choice == "5":
                self.wallet.create_keys()
                self.blockchain = Blockchain(self.wallet.public_key)
            elif user_choice == "6":
                self.wallet.load_keys()
                self.blockchain = Blockchain(self.wallet.public_key)
            elif user_choice == "7":
                self.wallet.save_keys()
            elif user_choice == "q":
                waiting_for_input = False
            else:
                print("Input invalid, please pick a valid option")
            if not Verification.verify_chain(self.blockchain.chain):
                self.print_blockchain_elements()
                print("Inválid blockchain")
                break
            print("Balance of {}: {:6.2f}".format(self.wallet.public_key, self.blockchain.get_balance()))
        else:
            print("User left")

        print("Done")

if __name__ == '__main__':
    node = Node()
    node.listem_for_input()
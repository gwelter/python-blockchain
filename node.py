class Node:
    def __init__(self):
        pass

    def get_transaction_value(self):
        """ Get the value entered by the user as a Float """
        tx_recipient = input("Enter the recipient of the transaction: ")
        tx_amount = float(input("Your transaction amount please: "))
        return tx_recipient, tx_amount


    def get_user_choice(self):
        """ Get the user choice """
        return input("Your choice: ")


    def print_blockchain_elements(self):
        for block in self.blockchain:
            print(block)
        else:
            print("-" * 20)


    def listem_for_input(self):
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
            user_choice = self.get_user_choice()
            if user_choice == "1":
                tx_data = self.get_transaction_value()
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
                self.print_blockchain_elements()
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
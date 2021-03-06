from hashlib import sha256
from datetime import date

def hash(string):
    return None if (string == None) else sha256(string.encode("ascii")).hexdigest()

class Transaction:
    def __init__(self, private_from_address, public_to_address, amount):
        self.private_from_address = private_from_address
        self.public_to_address = public_to_address
        self.amount = amount

    def __str__(self):
        return f"\t{str(self.private_from_address)} -> ${str(self.amount)} -> {str(self.public_to_address)}"

    def __repr__(self):
        return str(self)
        
class Block:
    def __init__(self, transactions, previous_hash):
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0;
        self.date = date.today()
        self.hash = ""

    def hash_recalc(self):
        header = str(self.nonce) + str(self.transactions) + str(self.previous_hash)
        return hash(header)

    def mineBlock(self, difficulty):
        while not self.hash.startswith("0" * difficulty):
            self.nonce += 1
            self.hash = self.hash_recalc()
            if self.nonce % 10000 == 0:
                print(self.nonce, end = '\r')
        print("nonce = " + str(self.nonce))

    def __str__(self):
        self.string = ""
        for i in self.transactions:
            self.string += str(i) + "\n"
        return self.string

class Blockchain:
    def __init__(self, difficulty, mining_reward):
        self.chain = [self.gen_block()]
        self.difficulty = difficulty
        self.pending_transactions = []
        self.mining_reward = mining_reward

    def gen_block(self):
        return Block([Transaction(None, None, 0)], 0)

    def latest_block(self):
        return self.chain[-1]

    def minePendingTransactions(self, public_to_address):
        newBlock = Block(self.pending_transactions, self.latest_block().hash)
        newBlock.mineBlock(self.difficulty)
        self.chain.append(newBlock)
        self.pending_transactions = [Transaction(None, public_to_address, self.mining_reward)]

    def balance_of_address(self, private_address):
        balance = 0
        public_address = hash(private_address)
        #add pending block to balance so to make sure no negative balance
        pending_chain = self.chain + [Block(self.pending_transactions, self.latest_block().hash)]
        for block in pending_chain:
            for trans in block.transactions:
                if(trans.private_from_address == private_address):
                    balance -= trans.amount
                if(trans.public_to_address == public_address):
                    balance += trans.amount
        return balance

    def addTransaction(self, transaction):
        if ((transaction.private_from_address != None) and (self.balance_of_address(transaction.private_from_address) < transaction.amount)):
            print(str(transaction) + "\nNot enough funds on address")
        else:   self.pending_transactions.append(transaction)

    def chain_validity(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            if(current_block.previous_hash != previous_block.hash):
                return False
            if(current_block.hash != current_block.hash_recalc()):
                return False
        return True

    def __str__(self):
        self.print = ""
        for i in self.chain:
            self.print += str(i) + "\n"
        return self.print

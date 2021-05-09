from hashlib import sha256
from datetime import date

def hash(string):
    if string == None:
        return None
    return sha256(string.encode("ascii")).hexdigest()


class Transaction:
    def __init__(self, from_address, to_address, amount):
        self.from_address = hash(from_address)
        self.to_address = hash(to_address)
        self.amount = amount

    def __str__(self):
        return f"\t{str(self.from_address)} -> ${str(self.amount)} -> {str(self.to_address)}"


class Block:
    def __init__(self, transactions, previous_hash):
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0;
        self.date = date.today()
        self.hash = ""

    def calcHash(self):
        header = str(self.date) + str(self.nonce) + str(self.transactions) + str(self.previous_hash)
        return hash(header)

    def mineBlock(self, difficulty):
        while not self.hash.startswith("0" * difficulty):
            self.nonce +=1
            self.hash = self.calcHash()

    def __str__(self):
        self.string = ""
        for i in self.transactions:
            self.string += str(i) + "\n"
        return self.string



class Blockchain:
    def __init__(self):
        self.chain = [self.createGenBlock()]
        self.difficulty = 2
        self.pending_transactions = []
        self.mining_reward = 100

    def createGenBlock(self):
        return Block([Transaction(None, None, 0)], 0)

    def latestBlock(self):
        return self.chain[-1]

    def minePendingTransactions(self, mining_reward_address):
        newBlock = Block(self.pending_transactions, self.latestBlock().hash)
        newBlock.mineBlock(self.difficulty)
        self.chain.append(newBlock)
        self.pending_transactions = [Transaction(None, mining_reward_address, self.mining_reward)]

    def balanceOfAddress(self, address):
        balance = 0
        #add pending block to balance
        pending_chain = self.chain + [Block(self.pending_transactions, self.latestBlock().hash)]
        for block in pending_chain:
            for trans in block.transactions:
                if(trans.from_address == address):
                    balance -= trans.amount
                if(trans.to_address == address):
                    balance += trans.amount
        return balance

    def addTransaction(self, transaction):
        if ((transaction.from_address != None) and (self.balanceOfAddress(transaction.from_address) < transaction.amount)):
            print(str(transaction) + "\nNot enough funds on address")
        else:   self.pending_transactions.append(transaction)

    def isChainValid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            if(current_block.previous_hash != previous_block.hash):
                return False
            if(current_block.hash != current_block.calcHash()):
                return False
        return True

    def __str__(self):
        self.print = ""
        for i in self.chain:
            self.print += str(i) + "\n"
        return self.print

from hashlib import sha256
import time



class Transaction:
    def __init__(self, from_address, to_address, amount):
        self.from_address = from_address
        self.to_address = to_address
        self.amount = amount



class Block:
    def __init__(self, transactions, previous_hash):
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0;
        self.hash = self.calcHash()

    def calcHash(self):
        header = str(self.nonce) + str(self.transactions) + str(self.previous_hash)
        return sha256(header.encode("ascii")).hexdigest()

    def mineBlock(self, difficulty):
        while(self.hash.startswith("0" * difficulty) == False):
            self.nonce +=1
            self.hash = self.calcHash()
        print(f"Successfully mined block: {self.hash}")




class Blockchain:
    def __init__(self):
        self.chain = [self.createGenBlock()]
        self.difficulty = 4
        self.pending_transactions = []
        self.mining_reward = 100

    def createGenBlock(self):
        return Block([Transaction(None, "0", 0)], 0)

    def getLatestBlock(self):
        return self.chain[-1]

    def minePendingTransactions(self, mining_reward_address):
        newBlock = Block(self.pending_transactions, self.getLatestBlock().hash)
        newBlock.mineBlock(self.difficulty)
        self.chain.append(newBlock)
        self.pending_transactions = [Transaction("0", mining_reward_address, self.mining_reward)]

    def createTransaction(self, transaction):
        self.pending_transactions.append(transaction)

    def getBalanceOfAddress(self, address):
        balance = 0
        for block in self.chain:
            for trans in block.transactions:
                if(trans.from_address == address):
                    balance -= trans.amount
                if(trans.to_address == address):
                    balance += trans.amount
        return balance

    def isChainValid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            if(current_block.previous_hash != previous_block.hash):
                return False
            if(current_block.hash != current_block.calcHash()):
                return False
        return True



def set_balance(address, amount):
    YCoin.createTransaction(Transaction(None, address, amount))

if __name__ == '__main__':

    YCoin = Blockchain()
    set_balance("1", 10000)
    YCoin.createTransaction(Transaction("1", "2", 50))
    YCoin.createTransaction(Transaction("2", "1", 60))
    YCoin.minePendingTransactions("1")
    YCoin.minePendingTransactions("1")

    print(YCoin.getBalanceOfAddress("1"))
    print(YCoin.getBalanceOfAddress("2"))

    #YCoin.chain[1].transactions = [Transaction("Dvir", "Yinon", 1000000)]
    print("Valid") if YCoin.isChainValid() else print("Unvalid")
